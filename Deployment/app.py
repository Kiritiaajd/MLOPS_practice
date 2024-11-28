from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

# Load the trained Linear Regression model
linear_model = pickle.load(open("linear.pkl", 'rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predicdata', methods=['GET', 'POST'])
def predit_datapoint():
    if request.method == "POST":
        # Get the form data for the three features
        feature1 = float(request.form['feature1'])
        feature2 = float(request.form['feature2'])
        feature3 = float(request.form['feature3'])

        # Scale the features if necessary (assuming scaling was applied to the model)
        # scaler = StandardScaler()
        # scaled_features = scaler.fit_transform([[feature1, feature2, feature3]])

        # Make the prediction using the loaded model
        prediction = linear_model.predict([[feature1, feature2, feature3]])[0]

        # Render home.html with the prediction result
        return render_template('home.html', prediction=prediction)
    
    # Render the form if it's a GET request
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
