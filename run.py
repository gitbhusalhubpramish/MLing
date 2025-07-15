import numpy as np

# Load model parameters
params = np.load("model_params.npz")
W1 = params["W1"]
b1 = params["b1"]
W2 = params["W2"]
b2 = params["b2"]
W3 = params["W3"]
b3 = params["b3"]

def load(input, w, b):
  return np.dot(input, w) + b

def main(input):
  output = load(load(load(input, W1, b1), W2, b2), W3, b3)
  print(output)