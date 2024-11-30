import pandas as pd

from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer

from sklearn.pipeline import make_pipeline



## Functions
# For re-label numerical values in the original data
def preprocess_cat_columns(data):
    data["Education"] = data["Education"].map({1:"Below College", 2:"College", 3:"Bachelor", 4:"Master",5:"Doctor"})
    data["JobInvolvement"] = data["JobInvolvement"].map({1:"Low", 2:"Medium", 3:"High", 4:"Very High"})
    return data


def num_pipeline_transformer(data):
    numerics = ['int64']
    num_attrs = data.select_dtypes(include=numerics)
    num_pipeline = Pipeline([
        ('std_scaler', StandardScaler()),
        ])
    return num_attrs, num_pipeline


def pipeline_transformer(data):
    cat_attrs = ["Education", "JobInvolvement", "BusinessTravel", "Gender", "JobRole"]
    num_attrs, num_pipeline = num_pipeline_transformer(data)
    # Make full_pipeline available at global scope for make_pipieline to use
    global full_pipeline
    full_pipeline = ColumnTransformer([
        ("num", num_pipeline, list(num_attrs)),
        ("cat", OneHotEncoder(), cat_attrs),
        ])
    prepared_data = full_pipeline.fit_transform(data)
    return prepared_data


def predict_attrition(config, model):
    if type(config) == dict:
        df_prep = config.copy()
        df = pd.DataFrame(df_prep, index=[0])
        print(df)
    else:
        df = config.copy()

    preproc_df = preprocess_cat_columns(df)
    print(preproc_df)
    # Read in and filter out columns from original data for use for the pipe
    attrition_df_temp = pd.read_csv("ml_models/data/IBM_attrition_data.csv")
    data_temp = attrition_df_temp.copy()
    data_temp_dropped_X = data_temp[["Age", "Education", "DistanceFromHome", "JobInvolvement", "HourlyRate", "JobRole", "Gender", "BusinessTravel"]].copy()
    data_temp_dropped_X_procc = preprocess_cat_columns(data_temp_dropped_X).copy()
    data_temp_dropped_Y = data_temp["Attrition"].copy()

    print(data_temp_dropped_X_procc)
    print(data_temp_dropped_Y)
    # Run pipeline_transformer once to make full_pipeline available for make_pipeline
    _ = pipeline_transformer(data_temp_dropped_X_procc)
    pipe = make_pipeline(full_pipeline, model)
    # Fit the pipe onto the original data to remember possible values for each categorical feature
    pipe.fit(data_temp_dropped_X_procc, data_temp_dropped_Y)
    print(df)
    y_pred = pipe.predict(df)

    print(y_pred)

    return y_pred


