import json
import matplotlib.pyplot as plt
import numpy as np
import time

# Load JSON
with open("data_noisy.json") as f:
    data = json.load(f)["data"]

# Set interactive mode on
plt.ion()

# Create a figure
fig, ax = plt.subplots()

for sample in data:
    # Reshape 784 flat list into 28x28
    image = np.array(sample["input"]).reshape((28, 28))

    # Clear and update plot
    ax.clear()
    ax.imshow(image, cmap="gray", vmin=0, vmax=1)
    ax.set_title(f"Label: {sample.get('output', '?')}")
    ax.axis("off")

    plt.draw()
    plt.pause(1)  # delay between images

plt.ioff()
plt.show()
