import numpy as np
import json
import matplotlib.pyplot as plt

# Activation functions
def relu(z):
    return np.maximum(0, z)

def relu_derivative(z):
    return (z > 0).astype(float)

def softmax(z):
    # Subtract max for numerical stability to prevent overflow with large exp values
    z_exp = np.exp(z - np.max(z, axis=-1, keepdims=True))
    return z_exp / np.sum(z_exp, axis=-1, keepdims=True)

def cross_entropy_derivative(pred, target):
    return pred - target 

# Categorical Cross-Entropy Loss
def categorical_cross_entropy_loss(output, target):
    """
    Calculates categorical cross-entropy loss.
    output: softmax probabilities (shape: (num_classes,))
    target: one-hot encoded true labels (shape: (num_classes,))
    """
    epsilon = 1e-10  # Small epsilon to prevent log(0)
    # Ensure probabilities are not exactly 0 or 1
    output = np.clip(output, epsilon, 1. - epsilon)
    return -np.sum(target * np.log(output))

def init_weights():
    """
    Initializes weights and biases for a 3-layer neural network
    (Input -> 16 hidden -> 16 hidden -> 10 output).
        """
    # W1: (neurons in layer 1, input features)
    b1 = np.zeros(16)
    # W2: (neurons in layer 2, neurons in layer 1)
    b2 = np.zeros(16)
    # W3: (output classes, neurons in layer 2)
    b3 = np.zeros(10)
    W1 = np.random.randn(16, 784) * np.sqrt(2. / 784)
    W2 = np.random.randn(16, 16) * np.sqrt(2. / 16)
    W3 = np.random.randn(10, 16) * np.sqrt(2. / 16)


    np.savez("model_params.npz", W1=W1, b1=b1, W2=W2, b2=b2, W3=W3, b3=b3)
    print("Model initialized and saved to model_params.npz")

# Backpropagation
def backward(x, y_true, z1, a1, z2, a2, z3, a3, W3, W2):
    """
    Performs backpropagation for a 3-layer neural network
    with ReLU activation in hidden layers and Softmax output.
    Uses gradient derived for Categorical Cross-Entropy Loss.
    """
    # For Softmax + Categorical Cross-Entropy, dL/dz3 = a3 - y_true
    dz3 = a3 - y_true            # (10,)
    dW3 = np.dot(dz3[:, np.newaxis], a2[np.newaxis, :])      # (10, 16)
    db3 = dz3                    # (10,)

    da2 = np.dot(W3.T, dz3)      # (16,)
    dz2 = da2 * relu_derivative(z2)
    dW2 = np.dot(dz2[:, np.newaxis], a1[np.newaxis,:])      # (16, 16)
    db2 = dz2

    da1 = np.dot(W2.T, dz2)      # (16,)
    dz1 = da1 * relu_derivative(z1)
    dW1 = np.dot(dz1[:, np.newaxis], x[np.newaxis,:])       # (16, 784)
    db1 = dz1

    return dW1, db1, dW2, db2, dW3, db3

# Training function
def train(X_train, y_train, learning_rate=0.001, epochs=100):
    """
    Trains the neural network model.

    Args:
        X_train (np.array): Training input data (normalized).
        y_train (np.array): One-hot encoded training target labels.
        learning_rate (float): Step size for weight updates.
        epochs (int): Number of training epochs.
    """
    # Load weights and biases
    try:
        params = np.load("model_params.npz")
        W1 = params["W1"]
        b1 = params["b1"]
        W2 = params["W2"]
        b2 = params["b2"]
        W3 = params["W3"]
        b3 = params["b3"]
        print("Model parameters loaded from model_params.npz")
    except FileNotFoundError:
        print("model_params.npz not found. Please run init_weights() first.")
        return

    # Ensure weights have correct shapes if they were saved in a different orientation
    # This assumes init_weights saves them correctly (output_dim, input_dim)
    # W1 (16, 784), W2 (16, 16), W3 (10, 16)
    # If there's still a shape mismatch, you might need more robust `fix_shape` or check save/load logic.

    max_grad_norm = 5.0 # Gradient clipping norm

    for epoch in range(epochs):
        epoch_loss = 0.0
        # Shuffle data each epoch for better training dynamics
        permutation = np.random.permutation(X_train.shape[0])
        X_shuffled = X_train[permutation]
        y_shuffled = y_train[permutation]

        correct_preds = 0
        for i in range(X_shuffled.shape[0]):
            x = X_shuffled[i].flatten() # Input features (784,)
            y_true = y_shuffled[i]      # One-hot encoded target (10,)

            # Forward pass
            z1 = np.dot(W1, x) + b1
            a1 = relu(z1)
            z2 = np.dot(W2, a1) + b2
            a2 = relu(z2)
            z3 = np.dot(W3, a2) + b3
            a3 = softmax(z3) # Output probabilities

            predicted_label = np.argmax(a3)
            actual_label = np.argmax(y_true)
            if predicted_label == actual_label:
                correct_preds += 1
                
            current_loss = categorical_cross_entropy_loss(a3, y_true)
            epoch_loss += current_loss

            # Backward pass
            dW1, db1, dW2, db2, dW3, db3 = backward(x, y_true, z1, a1, z2, a2, z3, a3, W3, W2)

            # Gradient Clipping (L2 norm clipping, but simple value clipping is used here)
            # Clip values to prevent them from becoming too large
            np.clip(dW1, -max_grad_norm, max_grad_norm, out=dW1)
            np.clip(db1, -max_grad_norm, max_grad_norm, out=db1)
            np.clip(dW2, -max_grad_norm, max_grad_norm, out=dW2)
            np.clip(db2, -max_grad_norm, max_grad_norm, out=db2)
            np.clip(dW3, -max_grad_norm, max_grad_norm, out=dW3)
            np.clip(db3, -max_grad_norm, max_grad_norm, out=db3)

            # Parameter update (Gradient Descent)
            W1 -= learning_rate * dW1
            b1 -= learning_rate * db1
            W2 -= learning_rate * dW2
            b2 -= learning_rate * db2
            W3 -= learning_rate * dW3
            b3 -= learning_rate * db3

        accuracy = correct_preds / X_train.shape[0]
        avg_epoch_loss = epoch_loss / X_shuffled.shape[0]
        print(f"Epoch {epoch+1}/{epochs}, Average Loss: {avg_epoch_loss:.8f}, Accuracy: {accuracy*100:.4f}%")


    # Save updated weights after training
    np.savez("model_params.npz", W1=W1, b1=b1, W2=W2, b2=b2, W3=W3, b3=b3)
    print("Training complete. Model saved to model_params.npz")
    print(f"Final W1 shape: {W1.shape}, b1 shape: {b1.shape}")
    print(f"Final W2 shape: {W2.shape}, b2 shape: {b2.shape}")
    print(f"Final W3 shape: {W3.shape}, b3 shape: {b3.shape}")

    # Main function
def main():
    with open('data.json', 'r') as f:
        raw = json.load(f)


    # Extract inputs and outputs
    X_raw = np.array([sample["input"] for sample in raw["data"]])
    y_raw = np.array([sample["output"] for sample in raw["data"]]) # Assuming raw output is integer class label

    # --- Data Preprocessing ---
    # 1. Normalize input features (assuming 0-255 pixel values)
    X_train = X_raw
    print(f"Input data (X) shape before flatten: {X_train.shape}")

    # 2. One-hot encode target labels (assuming 10 classes)
    num_classes = 10 # Adjust if your dataset has a different number of output classes
    y_train = np.zeros((y_raw.shape[0], num_classes))
    # Ensure y_raw elements are integers for indexing
    y_train[np.arange(y_raw.shape[0]), y_raw.astype(int)] = 1
    print(f"Target data (y) shape (one-hot encoded): {y_train.shape}")
    # --- End Preprocessing ---

    # Start training
    # Start with a conservative learning rate and increase if loss decreases too slowly
    # Given your dataset size, the learning process will be very noisy.
    # Try 0.001 or 0.0005 initially.
    train(X_train, y_train, learning_rate=0.01, epochs=1000)
    print(f"Loaded data with {len(raw['data'])} samples.")



if __name__ == "__main__":
    # Run init_weights() once to create the initial model_params.npz file.
    # If model_params.npz already exists and you want to continue training from it,
    # comment out or remove this line.
    # init_weights()
    main()