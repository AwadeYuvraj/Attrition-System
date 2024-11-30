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
## Comment out when using live ver.
from config import username, password
import os

# Query functions to be applied to the separate api routes
from data_query import dummy_data_query, raw_data_query
# from data_query import grades_dummy_query

# For secure/live ops version deployment
from flask_sqlalchemy import SQLAlchemy
from models import create_dummy_classes
from models import create_raw_classes
from test_alg_1 import predictor_func

import datetime
import pytz

####################################
# Begin Flask app setup
####################################
# Set up Flask app
app = Flask(__name__)

# from flask_debug import Debug
# Debug(app)
# app.run(debug=True)
####################################
# Setup database connection
####################################
# DEV/EDUCATIONAL VERSION
# Use SQLAlchemy to connect to postgreSQL server
engine = create_engine("postgresql://" + username + ":" + password + "@ec2-3-233-7-12.compute-1.amazonaws.com:5432/dfhhj9j187pecn")
conn = engine.connect()
Base = automap_base()
Base.prepare(engine, reflect=True)
session = Session(bind=engine)
dummy_class = Base.classes.dummy_data
raw_class = Base.classes.raw_data
## Test class
## Grade_data_dummy = Base.classes.grade_data_dummy


# # # SECURE/LIVE OPS VERSION
# # To be used if the online live app's login needs to be secure
# # Set up database connection
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '').replace("://", "ql://", 1)
# # Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# # Will need to switch to using models.py to create classes instead of sqlAlchemy reflectiosn
# dummy_class = create_dummy_classes(db)
# raw_class = create_raw_classes(db)


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


@app.route("/results.html")
def results():
    return render_template("results.html")

# @app.route("/predictor.html")
# def predictor():
#     return render_template("predictor.html")



# main_data_output = dummy_data_query(db.session, dummy_class)
# print(main_data_output)
# Routes for data queries to be used by JS apps


data_dict = {
    "dict_val1" : None,
    "dict_val2" : None
}

# Data retrieval from server
# Remove "db." when switching to dev version
@app.route("/api/dummy")
def dummy():
    dummy_data_output = dummy_data_query(session, dummy_class)
    return jsonify(dummy_data_output)

@app.route("/api/raw")
def raw():
    raw_data_output = raw_data_query(session, raw_class)
    return jsonify(raw_data_output)


# # Predictor test to send to predictor
# @app.route("/send", methods=["GET", "POST"])
# def send():
#     if request.method == "POST":
#         val1_data = request.form["val_1_form_name"]
#         val2_data = request.form["val_2_form_name"]
#         data_dict["dict_val1"] = val1_data
#         data_dict["dict_val2"] = val2_data
#         return redirect("/", code=302)
#     return render_template("form.html")


# # Predictor test to receive from predictor. Activates on user input from "send" route,
# #after the user submits information
# @app.route("/receive")
# def receive():
#     response = predictor_func(data_dict["dict_val1"], data_dict["dict_val2"])
#     return jsonify(response)


# Combined predictor route to post back out into HTML
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        # check on if all types are correct
        # add all values into object
        val1_data = request.form["val_1_form_name"]
        val2_data = request.form["val_2_form_name"]
        data_dict["dict_val1"] = val1_data
        data_dict["dict_val2"] = val2_data
        response = predictor_func(request.form["val_1_form_name"], request.form["val_2_form_name"])
        prob_output = response["probability"]
        predict_output = response["prediction"]


        return render_template("form.html", prob_text = prob_output, predict_text = predict_output)
        # return render_template("results.html", prob_text = prob_output, predict_text = predict_output)
        # return redirect("/", code=302)
    return render_template("results.html")


# Predictor test to receive from predictor. Activates on user input from "send" route,
#after the user submits information
@app.route("/receive")
def receive():
    response = predictor_func(data_dict["dict_val1"], data_dict["dict_val2"])
    return jsonify(response)






# # POST test
# @app.route("/send", methods=["GET", "POST"])
# def send():
#     gmt_tz = pytz.timezone("GMT")

#     if request.method == "POST":
#         item_data_int_col = request.form["item_int_col"]
#         item_data_float_col = request.form["item_float_col"]
#         item_data_string_col = request.form["item_string_col"]
#         item_data_bool_col = bool(request.form["item_bool_col"])
#         item_data_na_col = request.form["item_na_col"]
#         item_data_time_col = gmt_tz.localize(datetime.datetime.strptime(request.form["item_time_col"], "%H:%M"))
#         item_data_latitude_col = request.form["item_latitude_col"]
#         item_data_longitude_col = request.form["item_longitude_col"]

#         item_record = dummy_class(
#             int_col = item_data_int_col,
#             float_col = item_data_float_col,
#             string_col = item_data_string_col,
#             bool_col = item_data_bool_col,
#             na_col = item_data_na_col,
#             time_col = item_data_time_col,
#             latitude_col = item_data_latitude_col,
#             longitude_col = item_data_longitude_col
#             )
#         session.add(item_record)
#         session.commit()
#         return redirect("/", code=302)
#     return render_template("form.html")



# Run app
if __name__ == "__main__":
    app.run()
