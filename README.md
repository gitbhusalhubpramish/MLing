# MLing

## Overview

**MLing** is a beginner-friendly interactive machine learning playground built with Python, NumPy, and Pygame. It allows users to **draw their own datasets**, train a neural network in real-time, and test predictions through a clean graphical interface.

Designed by **Pramish Bhusal**, a 13-year-old self-taught ML enthusiast, this project showcases how deep learning concepts can be made accessible and intuitive—even when running on constrained platforms like Replit.

This project is perfect for:
- Students learning ML basics
- Educators demonstrating neural nets live
- Developers experimenting with hand-drawn digits
- Curious learners who want to build a digit recognizer from scratch

---

## ✨ Features

- 🎨 **Draw Your Own Dataset**: Handwrite digits 0–9 directly in the UI.
- 🧠 **Train Neural Nets From Scratch**: No TensorFlow or PyTorch—just NumPy.
- 📈 **Live Accuracy & Loss Stats**: Training updates printed every epoch.
- 🌀 **Noise Augmentation**: Adds sparse noise to improve generalization.
- 💾 **Model Persistence**: Save and load trained model parameters easily.
- 🔍 **Instant Predictions**: Visualize what your model "sees" and guesses.
- 🧪 **Manual Dataset Building**: Collect over 8,000+ samples interactively.
- 🌐 **Runs on Replit**: Trained and tested entirely on a free, online IDE.
- ⚡ **Optimized for Learning**: Ideal for visual understanding of how models learn.

---

## 🚀 Quick Start

### Requirements

- Python 3.8+
- `pygame`, `numpy`, `matplotlib`

```bash
pip install pygame numpy matplotlib
```
### Run the App
```bash
python main.py
```
---
## 🧠 Neural Network Architecture

| Layer        | Size         | Activation |
|--------------|--------------|------------|
| Input        | 784 (28x28)  | –          |
| Hidden (1)   | 16           | ReLU       |
| Hidden (2)   | 16           | ReLU       |
| Output       | 10           | Softmax    |


- Loss: Categorical Cross-Entropy

- Optimizer: Custom Gradient Descent

- Techniques: Gradient Clipping, Sparse Noise, Manual Labeling

---

## 🗂️ Project Structure
```bash
MLing/
├── main.py                # Launches the GUI
├── window/
│   ├── main.py            # Pygame UI logic
│   └── buttons/           # UI buttons (reset, getdata, train, run, etc.)
├── train.py               # Training logic for the neural net
├── run.py                 # Inference module
├── add_noise.py           # Sparse noise injector
├── data.json              # Stored training data
└── model_params.npz       # Saved weights
```
## 🧪 How It Works
1. **Collect Data**

- Draw digits in the UI.

- Assign label (0–9) in terminal.

- Data saved in data.json.

2. **Augment Dataset**

- Run: `python add_noise.py`

- Injects controlled noise to improve training.

3. **Train the Model**

- Run: `python train.py`

- Monitors accuracy, loss, and learning rate every epoch.

- Trained on 8,800+ samples in over 1000+ epochs.

- Accuracy reaches **89%–100%** on in-distribution data, and **70%–80%** on out-of-distribution samples.

4. **Run Predictions**

- Click **Run** in the UI to infer from your drawings.

- Output printed and shown graphically.

## 🎯 Behind the Scenes
This project is built entirely from scratch by a 13-year-old aspiring ML engineer, trained and tested entirely on **Replit**, a limited online coding environment. Despite constraints like low performance and long training times, the model was trained on over **8,800 samples**—demonstrating resilience, curiosity, and creativity.

🧑‍💻 *“I trained this fully-connected model for 1000 epochs on Replit. It was slow, but I reached 89–100% accuracy. Even out-of-dataset predictions work around 70–80%!”* — Pramish

## 🙌 Contributing
Pull requests and ideas are always welcome.
Open an issue if you encounter bugs, need help, or want to suggest a new feature.

## 👨‍🎓 Author
Pramish Bhusal
13-year-old self-taught ML explorer & Python developer
GitHub: [@gitbhusalhubpramish](https://github.com/gitbhusalhubpramish)

## 📢 Feedback Wanted
If you're a professional ML engineer or educator, your feedback could help improve this open-source learning tool.
Feel free to open an issue or connect on GitHub.
