import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.stattools import durbin_watson


# Predicts number of readmissions using the number of discharges as a predictor.
def linear_model(health_df):
    X = health_df["Number of Discharges"]
    y = health_df["Number of Readmissions"]
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    y_pred = model.predict(X)

    fig, ax = plt.subplots()
    ax.scatter(health_df["Number of Discharges"], health_df["Number of Readmissions"], color='darkorange')
    ax.plot(health_df["Number of Discharges"], y_pred, color='teal')

    ax.set_xlabel("Number of Discharges", fontsize=16, fontname="Lucida Sans Unicode")
    ax.set_ylabel("Number of Readmissions", fontsize=16, fontname="Lucida Sans Unicode")
    ax.set_title("Number of Readmissions vs. Number of Discharges", fontsize=20, fontname="Lucida Sans Unicode")
    
    
# Predicts number of readmissions using the excess readmission ratio as a predictor.
def linear_model_2(health_df):
    X = health_df[["Excess Readmission Ratio"]]
    y = health_df["Number of Readmissions"]
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    y_pred = model.predict(X)

    plt.figure()
    plt.scatter(health_df["Excess Readmission Ratio"], y, color='darkorange')
    plt.plot(health_df["Excess Readmission Ratio"], y_pred, color='teal')
        
    plt.xlabel("Excess Readmission Ratio", fontsize=16, fontname="Lucida Sans Unicode")
    plt.ylabel("Number of Readmissions", fontsize=16, fontname="Lucida Sans Unicode")
    plt.title("Number of Readmissions vs. Excess Readmission Ratio", fontsize=20, fontname="Lucida Sans Unicode")


def residual_plot(health_df):
    X = health_df["Number of Discharges"]
    y = health_df["Number of Readmissions"]
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    y_pred = model.predict(X)
    
    plt.figure()
    plt.scatter(y_pred, model.resid, color="darkorange")
    plt.axhline(0, linestyle='--', color='teal')
    plt.xlabel("Fitted values", fontsize=16, fontname="Lucida Sans Unicode")
    plt.ylabel("Residuals", fontsize=16, fontname="Lucida Sans Unicode")
    plt.title("Residual Plot", fontsize=20, fontname="Lucida Sans Unicode")
    

# Referenced the following website for this function: https://www.datacamp.com/tutorial/variance-inflation-factor
def check_collinearity(health_df, p1, p2):
    X = sm.add_constant(health_df[[p1, p2]])
    vif = pd.DataFrame()
    vif["Variable"] = X.columns
    vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    print(vif)


def d_watson(health_df):
    X = sm.add_constant(health_df[["Number of Discharges", "Expected Readmission Rate"]])
    model = sm.OLS(health_df["Number of Readmissions"], X).fit()
    print()
    print("Durbin Watson of Number of Discharges and Expected Readmission Rate", durbin_watson(model.resid))
    print()


def main():
    health_df = pd.read_csv("FY_2025_Hospital_Readmissions_Reduction_Program_Hospital.csv")
    
    health_df = health_df[health_df["Number of Readmissions"] != "Too Few to Report"]
    health_df = health_df.dropna(subset=["Expected Readmission Rate", "Number of Readmissions", "Number of Discharges", 
                                        "Excess Readmission Ratio"])
    health_df["Number of Readmissions"] = health_df["Number of Readmissions"].astype(int)

    health_df["Start Date"] = pd.to_datetime(health_df["Start Date"])
    health_df["End Date"] = pd.to_datetime(health_df["End Date"])
    
    
    linear_model(health_df)
    residual_plot(health_df)
    check_collinearity(health_df, "Number of Discharges", "Expected Readmission Rate")
    d_watson(health_df)
    linear_model_2(health_df)
    check_collinearity(health_df, "Excess Readmission Ratio", "Expected Readmission Rate")

    plt.show()


if __name__ == "__main__":
    main()
