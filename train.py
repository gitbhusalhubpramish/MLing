import numpy as np

params = np.load("model_params.npz")

def loss(output, target):
  return np.mean((output-target)**2)

def relu(z): return np.maximum(0, z)
def relu_derivative(z): return (z > 0).astype(float)
def softmax(z): return np.exp(z) / np.sum(np.exp(z))
def sigmodi(z): return 1 / (1 + np.exp(-z))
  
def backward(x, y_true, z1, a1, z2, a2, z3, a3, W3, W2):
  # a3: softmax output
  dz3 = a3 - y_true           # (10,) softmax derivative with cross-entropy
  dW3 = np.outer(dz3, a2)     # (10,16)
  db3 = dz3                   # (10,)

  da2 = np.dot(W3.T, dz3)     # (16,)
  dz2 = da2 * relu_derivative(z2)  # (16,)
  dW2 = np.outer(dz2, a1)     # (16,16)
  db2 = dz2                   # (16,)

  da1 = np.dot(W2.T, dz2)     # (16,)
  dz1 = da1 * relu_derivative(z1)  # (16,)
  dW1 = np.outer(dz1, x)      # (16,784)
  db1 = dz1                   # (16,)

  return dW1, db1, dW2, db2, dW3, db3


def train(X_train, y_train, X_test, y_test, learning_rate=0.1, epochs=10):
  W1 = params["W1"]
  b1 = params["b1"]
  W2 = params["W2"]
  b2 = params["b2"]
  W3 = params["W3"]
  b3 = params["b3"]
  for epoch in range(epochs):
    for i in range(X_train.shape[0]):
      x = X_train[i]
      y_true = y_train[i]
      z1 = np.dot(W1, x) + b1
      a1 = relu(z1)
      z2 = np.dot(W2, a1) + b2
      a2 = softmax(z2)
      z3 = np.dot(W3, a2) + b3
      a3 = sigmodi(z3)
      dW1, db1, dW2, db2, dW3, db3 = backward(x, y_true, z1, a1, z2, a2, W2,z3, a3, W3)
      W1 -= learning_rate * dW1
      b1 -= learning_rate * db1
      W2 -= learning_rate * dW2
      b2 -= learning_rate * db2
      W3 -= learning_rate * dW3
      b3 -= learning_rate * db3
      if i % 1000 == 0:
        print(f"Epoch {epoch}, Iteration {i}, Loss: {loss(a3, y_true)}")