# 🌠 Cosmic Compass: Asteroid Trajectory Forecasting System

**Cosmic Compass** is a high-performance deep learning system designed to predict the **3D trajectory of Near-Earth Asteroids (NEAs)**.  
By leveraging **Long Short-Term Memory (LSTM)** networks, the system overcomes the latency bottlenecks of traditional physics-based solvers, delivering **millisecond-level inference with near-perfect accuracy**.

---

## 🚀 Key Highlights

- **⚡ High-Speed Inference**  
  Reduces prediction time from seconds/minutes (numerical integration) to **~50 ms**.

- **🎯 Superior Precision**  
  Achieved a **Mean Absolute Percentage Error (MAPE) of 0.1069%** on unseen test data  
  → **Predictive accuracy: 99.8931%**

- **🔁 End-to-End Pipeline**  
  - Automated data acquisition from **JPL HORIZONS**
  - Optimized **LSTM-based prediction engine**
  - Interactive **3D web visualization** using **Plotly.js**

---

## 🛠️ Technical Stack

### 🔬 Deep Learning
- TensorFlow  
- Keras (Stacked LSTM Architecture)

### ⚙️ Backend
- Python  
- Flask (RESTful Inference Service)

### 🌐 Frontend
- JavaScript  
- Plotly.js (Scientific 3D Visualization)  
- HTML5 / CSS3

### 📊 Data Engineering
- NumPy  
- Scikit-learn (`MinMaxScaler`)

### ☁️ Infrastructure
- **Render** – Backend API hosting  
- **Vercel** – Frontend deployment

---

## 🧠 Project Architecture

The system follows a **modular three-tier architecture**:

### 1️⃣ Data Tier
- Fetches **7 years of daily** asteroid position data  
- Coordinates: **X, Y, Z**
- Target object: **Asteroid 433 Eros**
- Data normalization using `MinMaxScaler`
- Structured via **Sliding Window Technique**  
  - **60-day input → 10-day forecast**

---

### 2️⃣ Model Tier
- **Stacked LSTM architecture**
  - 2 LSTM layers
  - 46 units per layer
- Optimized learning rate: **0.0001**
- Captures **non-linear orbital momentum**
- **34,042 trainable parameters**

---

### 3️⃣ Service Tier
- Flask-based REST API
- Serves:
  - Serialized LSTM model
  - Trained scaler
- Provides **low-latency real-time predictions**

> The LSTM architecture was chosen for its superior ability to model **long-term temporal dependencies**, which are essential for predicting **elliptical orbital dynamics** and enabling **reliable planetary defense systems**.

---

## 💻 Installation & Setup

### ✅ Prerequisites
- Python **3.8+**
- GitHub account (for deployment)

---

### 🔧 Backend Setup

#### Clone the repository
```bash
git clone https://github.com/yourusername/cosmic-compass.git
cd cosmic-compass
pip install -r requirements.txt
python app.py
```

#### Install dependencies
```bash
pip install -r requirements.txt
```

#### Start the Flask server
```bash
python app.py
```


### 🌐 Frontend Setup

-Open index.html in your browser
-Ensure the fetch() URL in your JavaScript file matches the backend API address

### 👥 Contributors

- Student 1: Data Engineering, Frontend Visualization, Unit Conversions

- Student 2: Model Core, Training Optimization, Flask API Development

- Student 3: System Architecture, Serialization, Integration Testing, Documentation



