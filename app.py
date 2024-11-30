####################################
# Import libraries
####################################
from flask import (
    Flask,
    render_template,
    # jsonify,
    request
    # redirect
)

from ml_models.final_model import predict_attrition
import pickle


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

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/form.html")
def form():
    return render_template("form.html")


# API routes
# Combined predictor route to post back out into HTML
@app.route('/send', methods=["GET", "POST"])
def predict():

    # Retreive finished prediction model
    with open('ml_models/attrition_prediction_model.bin', 'rb') as file:
        model = pickle.load(file)
        file.close()
    # Parse through form request
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

        # Execute prediction using form data and finished model
        response = predict_attrition(data_dict, model)[0]

    # Return prediction response
    return render_template("form.html", response_text = response)


# Run app
if __name__ == "__main__":
    app.run(debug = True)
