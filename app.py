import numpy as np
import tensorflow as tf
import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

try:
    model = tf.keras.models.load_model('asteroid_model.h5')
    
    with open('data_scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
        
    print("Model and scaler loaded successfully.")
except Exception as e:
    print(f"Error loading model or scaler: {e}")
    model = None
    scaler = None

INPUT_LENGTH = 60
OUTPUT_LENGTH = 10


@app.route('/predict', methods=['POST'])
def predict():
    if not model or not scaler:
        return jsonify({'error': 'Model or scaler not loaded'}), 500

    try:
        
        data = request.get_json()
        input_sequence = np.array(data['sequence'])

        
        if input_sequence.shape != (INPUT_LENGTH, 3):
            return jsonify({'error': f'Invalid input shape. Expected (60, 3), but got {input_sequence.shape}'}), 400

       
        normalized_input = scaler.transform(input_sequence)
        
      
        model_input = np.reshape(normalized_input, (1, INPUT_LENGTH, 3))
        
    
        normalized_prediction = model.predict(model_input)
        
      
        prediction_km = scaler.inverse_transform(normalized_prediction.reshape(OUTPUT_LENGTH, 3))
        
    
        return jsonify({'prediction': prediction_km.tolist()})

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


if __name__ == '__main__':
    print("Starting Flask server... Go to http://127.0.0.1:5000/")
    app.run(debug=True, port=5000)