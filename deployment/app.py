from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load('kmeans_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = float(request.form['age'])
        frequency = float(request.form['frequency'])
        spend = float(request.form['spend'])

        input_data = np.array([[age, frequency, spend]])
        scaled = scaler.transform(input_data)
        cluster = int(model.predict(scaled)[0])

        return render_template('index.html', cluster=cluster)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
