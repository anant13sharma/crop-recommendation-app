from flask import Flask, render_template, request
import joblib
import numpy as np

# Initialize app
app = Flask(__name__)

# Load model, scaler, and label encoder
model = joblib.load('Model/crop_recommendation_model.pkl')
scaler = joblib.load('Model/scaler.pkl')
label_encoder = joblib.load('Model/label_encoder.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from form
        input_data = [
            float(request.form['N']),
            float(request.form['Fe']),
            float(request.form['Mn']),
            float(request.form['S']),
            float(request.form['Mg']),
            float(request.form['C']),
            float(request.form['P']),
            float(request.form['K']),
            float(request.form['temperature']),
            float(request.form['humidity']),
            float(request.form['ph']),
            float(request.form['rainfall'])
        ]

        # Reshape and scale
        input_array = np.array(input_data).reshape(1, -1)
        input_scaled = scaler.transform(input_array)

        # Predict
        prediction = model.predict(input_scaled)[0]
        crop_name = label_encoder.inverse_transform([prediction])[0]

        return render_template('index.html', prediction=crop_name)

    except Exception as e:
        return render_template('index.html', prediction=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
