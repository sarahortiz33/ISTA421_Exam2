import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor


# Number of Discharges are floats
# Number of Readmissions were strings but I converted them to ints
# Predicted Readmission Rate is a float

# from the residual plot, it is clear that there are some outliers and that there is a funnel shape present.
# The funnel shape indicates non-constant variance of error terms. 
# No multicollinearity is present



health_df = pd.read_csv("FY_2025_Hospital_Readmissions_Reduction_Program_Hospital.csv")

health_df = health_df[health_df["Number of Readmissions"] != "Too Few to Report"]
health_df = health_df.dropna(subset=["Expected Readmission Rate", "Number of Readmissions", "Number of Discharges", 
                                     "Predicted Readmission Rate"])
health_df["Number of Readmissions"] = health_df["Number of Readmissions"].astype(int)

health_df["Start Date"] = pd.to_datetime(health_df["Start Date"])
health_df["End Date"] = pd.to_datetime(health_df["End Date"])
#print(health_df.head(10))


for i in health_df["Predicted Readmission Rate"]:
    print(type(i))


# response variable is the number of readmissions


def linear_model(health_df):
    X = health_df["Number of Discharges"]
    y = health_df["Number of Readmissions"]
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    y_pred = model.predict(X)

    fig, ax = plt.subplots()
    ax.scatter(health_df["Number of Discharges"], health_df["Number of Readmissions"], color='darkorange')
    ax.plot(health_df["Number of Discharges"], y_pred, color='teal')
        
    ax.set_facecolor("floralwhite")
    ax.set_xlabel("Number of Discharges", fontsize=16, fontname="Lucida Sans Unicode")
    ax.set_ylabel("Number of Readmissions", fontsize=16, fontname="Lucida Sans Unicode")
    ax.set_title("Number of Readmissions vs. Number of Discharges", fontsize=20, fontname="Lucida Sans Unicode")
    fig.patch.set_facecolor("whitesmoke")
    print(model.summary())



def residual_plot(y_pred, model):
    X = health_df["Number of Discharges"]
    y = health_df["Number of Readmissions"]
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    y_pred = model.predict(X)
    
    plt.figure()
    plt.scatter(y_pred, model.resid, color="darkorange")
    plt.axhline(0, linestyle='--', color='blue')
    plt.xlabel("Fitted values")
    plt.ylabel("Residuals")
    plt.title("Residual Plot")
    

# Referenced the following website for this function: https://www.datacamp.com/tutorial/variance-inflation-factor
def check_collinearity(health_df):
    X = sm.add_constant(health_df[["Number of Discharges", "Expected Readmission Rate"]])
    vif = pd.DataFrame()
    vif["Variable"] = X.columns
    vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    print(vif)





def main():
    #linear_model(health_df)
    #residual_plot(health_df["Number of Readmissions"], health_df["Number of Discharges"])
    check_collinearity(health_df)
    plt.show()


if __name__ == "__main__":
    main()
