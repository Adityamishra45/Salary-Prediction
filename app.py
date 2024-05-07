from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the pre-trained logistic regression model
with open("C:/Users/hp/Desktop/Data Science By CodeBasics/Machine Learning/8- Logistic Regression (Multi class)/model.pkl", 'rb') as f:
    model = pickle.load(f)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the form
    features = [float(x) for x in request.form.values()]
    input_features = [np.array(features)]

    # Make prediction using the loaded model
    prediction = model.predict(input_features)

    # Map the prediction to the corresponding salary category
    if prediction == 0:
        salary_category = 'Low'
    elif prediction == 1:
        salary_category = 'Medium'
    else:
        salary_category = 'High'

    return render_template('index.html', prediction_text='Predicted Salary Category: {}'.format(salary_category))

if __name__ == '__main__':
    app.run(debug=True)
