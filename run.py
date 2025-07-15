import numpy as np

# Load model parameters
params = np.load("model_params.npz")
W1 = params["W1"]
b1 = params["b1"]
W2 = params["W2"]
b2 = params["b2"]
W3 = params["W3"]
b3 = params["b3"]

def relu(x):
  return np.maximum(0, x)
def softmax(x):
  exp_x = np.exp(x - np.max(x))
  return exp_x / exp_x.sum(axis=0)
def sigmodi(x):
  return 1 / (1 + np.exp(-x))

def load(input, w, b, fun):
  return np.dot(input, w) + b if fun == "relu" else sigmodi(np.dot(input, w) + b) if fun == "sigmodi" else softmax(np.dot(input, w) + b)

def main(input):
  output = load(load(load(input, W1, b1, "softmax"), W2, b2, "relu"), W3, b3, "sigmodi")
  print(output)