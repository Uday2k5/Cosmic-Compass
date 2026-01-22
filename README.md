Cosmic Compass: Asteroid Trajectory Forecasting System 🌠

Cosmic Compass is a high-performance deep learning system designed to predict the 3D trajectory of Near-Earth Asteroids (NEAs). By leveraging Long Short-Term Memory (LSTM) networks, the system overcomes the latency bottlenecks of traditional physics-based solvers, providing millisecond-level inference with 99.90% accuracy.

🚀 Key Highlights

High-Speed Inference: Reduces prediction time from seconds/minutes (numerical integration) to milliseconds (~50ms).

Superior Precision: Achieved a Mean Absolute Percentage Error (MAPE) of 0.1069% on unseen test data, representing a predictive accuracy of 99.8931%.

End-to-End Pipeline: Includes automated data acquisition from JPL HORIZONS, an optimized LSTM-based prediction engine, and an interactive 3D web visualization using Plotly.js.

🛠️ Technical Stack

Deep Learning: TensorFlow, Keras (Stacked LSTM Architecture)

Backend: Python, Flask (RESTful Inference Service)

Frontend: JavaScript, Plotly.js (Scientific 3D Visualization), HTML5/CSS3

Data Engineering: NumPy, Scikit-learn (MinMaxScaler)

Infrastucture: Render (Backend API), Vercel (Frontend Hosting)

📂 Project Architecture

The system follows a modular three-tier architecture:

Data Tier: Fetches 7 years of daily $X, Y, Z$ coordinates for asteroid 433 Eros. Data is normalized using MinMaxScaler and structured using a Sliding Window Technique (60-day input $\to$ 10-day forecast).

Model Tier: A Stacked LSTM model (two layers, 46 units each) trained with an optimized learning rate ($0.0001$) to capture non-linear orbital momentum across 34,042 trainable parameters.

Service Tier: A Flask API that serves the serialized model and scaler, providing a low-latency RESTful endpoint for real-time predictions.

📊 Results & Evaluation

The model was evaluated against a Gated Recurrent Unit (GRU) model to justify the architecture choice:

Metric

LSTM (Selected)

GRU (Baseline)

Accuracy (MAPE)

99.90%

99.88%

Inference Latency

~50ms

~40ms

Stability

High

Medium

The LSTM was chosen for its superior ability to handle long-term temporal dependencies in elliptical orbits, essential for reliable planetary defense.

💻 Installation & Setup

Prerequisites

Python 3.8+

GitHub Account (for deployment)

Backend Setup

Clone the repository:

git clone [https://github.com/yourusername/cosmic-compass.git](https://github.com/yourusername/cosmic-compass.git)
cd cosmic-compass


Install dependencies:

pip install -r requirements.txt


Start the Flask server:

python app.py


Frontend Setup

Open index.html in your browser (via Live Server or similar).

Ensure the fetch() URL in your JavaScript matches your backend address.

👥 Contributors

Student 1: Data Engineering, Frontend Visualization, Unit Conversions.

Student 2: Model Core, Training Optimization, Flask API Development.

Student 3: System Architecture, Serialization, Integration Testing, Documentation.

📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

Developed as a Development-cum-Research project for advancing planetary defense monitoring systems.