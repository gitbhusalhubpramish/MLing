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

def load(input, w, b, fun):
  z = np.dot(w, input) + b
  if fun == "relu":
      return relu(z)
  elif fun == "softmax":
      return softmax(z)
  else:
      return z

def forward(input):
    a1 = load(input, W1, b1, "relu")
    a2 = load(a1, W2, b2, "relu")
    a3 = load(a2, W3, b3, "softmax")
    z1 = np.dot(W1, input) + b1
    z2 = np.dot(W2, a1) + b2
    z3 = np.dot(W3, a2) + b3
    return a1, z1, a2, z2, a3, z3

def main(input, obj):
  a1 = load(input, W1, b1, "relu")
  a2 = load(a1, W2, b2, "relu")
  a3 = load(a2, W3, b3, "softmax")
  obj.output = a3
  print(obj.output)
