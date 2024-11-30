Employee Attrition Prediction Web App
This project demonstrates the use of machine learning to predict employee attrition based on various employee attributes. It is an educational web app designed to help organizations predict employee turnover and understand key factors influencing attrition. Built using Python, Flask, and machine learning models, this web app provides users with interactive data inputs and predictions.

Features
Employee Attrition Prediction: Enter employee data to predict whether an employee is likely to leave the organization.
Data Visualization: Interactive charts to explore the relationship between employee features (e.g., job satisfaction, education level) and attrition risk.
Machine Learning Model: Uses a Random Forest model trained on the IBM HR Analytics dataset.
User-Friendly Interface: A dashboard displaying insights and a form to submit employee data for prediction.
Technologies Used
Python (Flask for web app backend)
Machine Learning (Random Forest model)
HTML/CSS/JavaScript (For frontend and user interaction)
MongoDB Charts (For data visualization)
Heroku (For hosting the web app)
Setup Instructions
To run the project locally:

Clone the repository:

git clone https://github.com/SanabuW/attrition_ML.git
cd attrition_ML
Install the required dependencies:

pip install -r requirements.txt
Run the app:

python app.py
Open the app in your browser at http://127.0.0.1:5000.

Usage
Prediction Form: Navigate to the "Attrition Predictor" page to input employee data and receive a prediction.
Dashboard: View visual insights into the dataset and understand correlations between employee features and attrition.
Data
The model is trained on the IBM HR Analytics dataset available here.
https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset
