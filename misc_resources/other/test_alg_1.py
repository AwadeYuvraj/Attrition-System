# %%
def predictor_func(val1, val2) :

    # To add a new cell, type '# %%'
    # To add a new markdown cell, type '# %% [markdown]'
    # %%
    from IPython import get_ipython

    # %% [markdown]
    # # Logistic Regression
    # 
    # Logistic Regression is a statistical method for predicting binary outcomes from data.
    # 
    # Examples of this are "yes" vs "no" or "young" vs "old". 
    # 
    # These are categories that translate to probability of being a 0 or a 1.
    # 
    # Source: [Logistic Regression](https://towardsdatascience.com/real-world-implementation-of-logistic-regression-5136cefb8125)
    # %% [markdown]
    # We can calculate logistic regression by adding an activation function as the final step to our linear model. 
    # 
    # This converts the linear regression output to a probability.

    # %%
    # get_ipython().run_line_magic('matplotlib', 'inline')
    import matplotlib.pyplot as plt
    import pandas as pd

    # %% [markdown]
    # Linear Regression:
    # <br>Y = β0+β1X
    # <br>Depending on the values of X (explanatory variable), the predict values for Y (response variable) may fall outside of \[ 0, 1 ]
    # <br>Changes in X have a linear effect on estimated probabilties
    # <br>Coefficients are easy to interpret, i.e., the change in Y when C increases by one unit
    # 
    # <br>Logistic Regression:
    # <br>P(Y=1) = e^(β0+β1X) / (1 + e^(β0+β1X))
    # <br>Predicted values always fall in \[ 0, 1 ]
    # <br>Changes in X can have a different effect on probabilities for different levels of X
    # <br>So, how to interpret Coefficients?
    # <br>The odds ratio for the estimated coefficient b1 is e^b1
    # <br>
    # <br>Probabilities (Wins / (Wins+loses))
    # <br>vs 
    # <br>Odds (Wins / Loses)
    # <br>
    # <br>0.50 1/2 --- 0.50/(1-0.50) 1
    # <br>0.33 1/3 --- 0.33/(1-0.33) 1/2
    # <br>0.66 2/3 --- 0.66/(1-0.66) 2
    # <br>0.20 1/5 --- 0.20/(1-0.2) 1/4

    # %%
    from sklearn.datasets import make_blobs

    X, y = make_blobs(centers=2, random_state=42)

    print(f"Labels: {y[:10]}")
    print(f"Data: {X[:10]}")


    # %%
    # Visualizing both classes
    plt.scatter(X[:, 0], X[:, 1], c=y)

    # %% [markdown]
    # Split our data into training and testing

    # %%
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    # %% [markdown]
    # Create a Logistic Regression Model

    # %%
    from sklearn.linear_model import LogisticRegression
    classifier = LogisticRegression()
    classifier

    # %% [markdown]
    # Fit (train) or model using the training data

    # %%
    classifier.fit(X_train, y_train)

    # %% [markdown]
    # Validate the model using the test data

    # %%
    # Mean Accuracy

    print(f"Training Data Score: {classifier.score(X_train, y_train)}")
    print(f"Testing Data Score: {classifier.score(X_test, y_test)}")

    # %% [markdown]
    # Make predictions

    # %%
    # Generate a new data point (the red circle)
    import numpy as np
    new_data1 = np.array([[-2, 6]])
    new_data2 = np.array([[-1, 6]])
    new_data3 = np.array([[1, 6]])
    new_data4 = np.array([[3, 6]])
    new_data5 = np.array([[val1, val2]])
    plt.scatter(X[:, 0], X[:, 1], c=y)
    plt.scatter(new_data1[0, 0], new_data1[0, 1], c="r", marker="o", s=100)
    plt.scatter(new_data2[0, 0], new_data2[0, 1], c="r", marker="o", s=100)
    plt.scatter(new_data3[0, 0], new_data3[0, 1], c="r", marker="o", s=100)
    plt.scatter(new_data4[0, 0], new_data4[0, 1], c="r", marker="o", s=100)

    # Predict the class (purple or yellow) of the new data point
    prediction1 = classifier.predict(new_data1)
    pred_prob1 = classifier.predict_proba(new_data1)[:, 1]
    pred_odds1 = pred_prob1/(1-pred_prob1)

    prediction2 = classifier.predict(new_data2)
    pred_prob2 = classifier.predict_proba(new_data2)[:, 1]
    pred_odds2 = pred_prob2/(1-pred_prob2)

    prediction3 = classifier.predict(new_data3)
    pred_prob3 = classifier.predict_proba(new_data3)[:, 1]
    pred_odds3 = pred_prob3/(1-pred_prob3)

    prediction4 = classifier.predict(new_data4)
    pred_prob4 = classifier.predict_proba(new_data4)[:, 1]
    pred_odds4 = pred_prob4/(1-pred_prob4)

    prediction5 = classifier.predict(new_data5)
    pred_prob5 = classifier.predict_proba(new_data5)[:, 1]
    pred_odds5 = pred_prob5/(1-pred_prob5)

    # %%
    print("Classes are either 0 (purple) or 1 (yellow)")
    print(f"The new point estimated probability is: {pred_prob1} {pred_prob2} {pred_prob3} {pred_prob4}  {pred_prob5}")
    print(f"The new point estimated odds is: {pred_odds1} {pred_odds2} {pred_odds3} {pred_odds4} {pred_odds5}")
    print(f"The new point was classified as: {prediction1} {prediction2} {prediction3} {prediction4} {prediction5}")

    # %%
    result_response = {
        "probability": f'{round(float(pred_prob5[0]), 4)*100}%',
        "prediction": int(prediction5[0])
    }

    # %%
    return result_response

    # # %%
    # import math
    # print(classifier.intercept_)

    # print(classifier.coef_[0])

    # odds_ratio = [ math.exp(x) for x in classifier.coef_[0]]
    # print(odds_ratio)


    # # %%
    # pred_odds1[0]*odds_ratio[0]


    # # %%
    # pred_odds2[0]/odds_ratio[0]


    # # %%
    # pred_odds1[0]*(odds_ratio[0])**5


    # # %%
    # # get importance
    # importance = classifier.coef_[0]
    # importance


    # # %%
    # for i,v in enumerate(importance):
    #     print('Feature: %0d, Score: %.5f' % (i,v))


    # # %%



