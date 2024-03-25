from flask import Flask, request, render_template
import numpy as np
import joblib

# Load the trained model
model = joblib.load('diabetesM.pkl')

app = Flask(__name__)

# Define the route for the home page
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Define the route for form submission and prediction
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form data and convert to float
        pregnancies = float(request.form['Pregnancies'])
        glucose = float(request.form['Glucose'])
        blood_pressure = float(request.form['BloodPressure'])
        skin_thickness = float(request.form['SkinThickness'])
        insulin = float(request.form['Insulin'])
        bmi = float(request.form['BMI'])
        diabetes_pedigree_function = float(request.form['DiabetesPedigreeFunction'])
        age = float(request.form['Age'])

        # Create feature array
        features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])

        # Make prediction
        result = model.predict(features)[0]

        # Convert prediction to human-readable format
        prediction_text = "Positive" if result == 1 else "Negative"

        # Render the template with the prediction result
        return render_template('index.html', result=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
