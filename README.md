<!-- # 🌌 Cosmic Compass (Project ATLAS)
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
└── README.md               # Project documentation -->


Cosmic Compass: Asteroid Trajectory Forecasting System 🌠

Cosmic Compass is a high-performance deep learning system designed to predict the 3D trajectory of Near-Earth Asteroids (NEAs). By leveraging Long Short-Term Memory (LSTM) networks, the system overcomes the latency bottlenecks of traditional physics-based solvers, providing millisecond-level inference with 99.90% accuracy.

🚀 Key Highlights

High-Speed Inference: Reduces prediction time from seconds/minutes (numerical integration) to milliseconds.

Superior Precision: Achieved a Mean Absolute Percentage Error (MAPE) of 0.10% on unseen test data.

End-to-End Pipeline: Includes data acquisition from JPL HORIZONS, an LSTM-based prediction engine, and an interactive 3D web visualization.

🛠️ Technical Stack

Deep Learning: TensorFlow, Keras (LSTM & GRU Architectures)

Backend: Python, Flask (Inference Service)

Frontend: JavaScript, Plotly.js (3D Visualization), HTML/CSS

Data Engineering: NumPy, Pandas, Scikit-learn (MinMaxScaler)

Data Source: NASA JPL HORIZONS System

📂 Project Architecture

The system follows a three-tier architecture:

Data Tier: Fetches 7 years of daily $X, Y, Z$ coordinates for asteroid 433 Eros. Data is normalized and structured using a Sliding Window Technique (60-day input $\to$ 10-day forecast).

Model Tier: A Stacked LSTM model trained with an optimized learning rate ($0.0001$) to capture non-linear orbital momentum and gravitational influences.

Service Tier: A Flask API that serves the serialized model and scaler, providing a RESTful endpoint for real-time predictions.

💻 Installation & Setup

Prerequisites

Python 3.8+

Node.js (for frontend serving)

Backend Setup

Clone the repository:

git clone https://github.com/Uday2k5/Cosmic-Compass
cd cosmic-compass


Install dependencies:

pip install -r requirements.txt


Start the Flask server:

python app.py


Frontend Setup

Open index.html in your browser (or use a Live Server extension).

Ensure the API URL in your JavaScript matches your Flask local address (http://127.0.0.1:5000).

👥 Contributors

Student 1: Data Engineering, Frontend Visualization (Plotly.js), Unit Conversions.

Student 2: Model Core, Training Optimization, Flask API Development.

Student 3: System Architecture, Serialization, Integration Testing, Documentation.