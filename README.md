# 🌌 Cosmic Compass (Project ATLAS)
### 3D Asteroid Trajectory Prediction Using Deep Learning

**Cosmic Compass** is an AI-powered system that predicts and visualizes asteroid trajectories in **3D space** using historical ephemeris data from **NASA JPL Horizons**.  
It leverages a **Long Short-Term Memory (LSTM)** neural network to forecast future orbital coordinates and renders them in an **interactive browser-based 3D environment**.

![Status](https://img.shields.io/badge/Status-Completed-success)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Key Features

- **AI-Based Prediction**  
  Stacked LSTM model trained on long-term asteroid ephemeris data.

- **Interactive 3D Visualization**  
  Explore asteroid motion using a rotatable, zoomable Plotly-based 3D graph.

- **Future Trajectory Forecasting**  
  Predicts **10 future time steps** from recent historical data.

- **High Accuracy**  
  Achieves **>99% accuracy** (MAPE < 0.1%) on test datasets.

- **Model Comparison Mode**  
  Compare **Ground Truth vs LSTM vs GRU** predictions.

---

## 📂 Project Structure

```text
cosmic-compass/
│
├── app.py                  # Flask backend (loads model & serves predictions)
├── app.js                  # Frontend logic for visualization
├── index.html              # Main UI
│
├── asteroid_model.h5       # Trained LSTM model
├── data_scaler.pkl         # Scikit-learn scaler for normalization
├── horizons_results.txt    # NASA JPL ephemeris data
│
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
