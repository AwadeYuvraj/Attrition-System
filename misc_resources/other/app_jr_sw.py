####################################
# Import libraries
####################################
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect
)
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

#CHANGE TO FINAL FILENAME LATER
# from ml_models.final_model import predict_attrition

from final_model_jr_sw import predict_attrition
import pickle
import numpy as np
## Comment out when using live ver.
import os

# Query functions to be applied to the separate api routes

# For secure/live ops version deployment
# from flask_sqlalchemy import SQLAlchemy
from test_alg_1 import predictor_func


####################################
# Begin Flask app setup
####################################
# Set up Flask app
app = Flask(__name__)

####################################
# Create/Define Flask app routes
####################################
# Front-end page routes
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/form.html")
def form():
    return render_template("form.html")

data_dict = {
    "dict_val1" : None,
    "dict_val2" : None
}

# APIs for data retrieval from server
# Remove "db." when switching to dev version

@app.route('/send', methods=["GET", "POST"])
def predict():

    with open('./ml_models/attrition_prediction_model.bin', 'rb') as file:
        model = pickle.load(file)
        file.close()
    if request.method == "POST":
        val1_data = int(request.form['Age'])
        val2_data = int(request.form['Education'])
        val3_data = int(request.form['DistanceFromHome'])
        val4_data = int(request.form['JobInvolvement'])
        val5_data = float(request.form['HourlyRate'])
        val6_data = str(request.form['JobRole'])
        val7_data = str(request.form['Gender'])
        val8_data = str(request.form['BusinessTravel'])

        data_dict = {"Age": val1_data,
                        "Education": val2_data,
                        "DistanceFromHome": val3_data,
                        "JobInvolvement": val4_data,
                        "HourlyRate": val5_data,
                        "JobRole": val6_data,
                        "Gender": val7_data,
                        "BusinessTravel": val8_data}

        response = predict_attrition(data_dict, model)

    return render_template("form.html", response_text = response[0])


# Run app
if __name__ == "__main__":
    app.run(debug = True)
