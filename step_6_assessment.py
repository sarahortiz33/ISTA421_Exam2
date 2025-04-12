import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


health_df = pd.read_csv("FY_2025_Hospital_Readmissions_Reduction_Program_Hospital.csv")
    
health_df = health_df[health_df["Number of Readmissions"] != "Too Few to Report"]
health_df = health_df.dropna(subset=["Expected Readmission Rate", "Number of Readmissions", "Number of Discharges",
                                     "Predicted Readmission Rate"])
health_df["Number of Readmissions"] = health_df["Number of Readmissions"].astype(int)


X = health_df[["Number of Discharges", "Expected Readmission Rate"]].values
y = health_df["Number of Readmissions"].values

mean_X = np.mean(X, axis=0)
std_X = np.std(X, axis=0)
X_norm = (X - mean_X) / std_X

X1 = X_norm[:, 0]  
X2 = X_norm[:, 1]

X1_squared = X1 ** 2          
X2_squared = X2 ** 2         
X1_X2_interaction = X1 * X2

X_poly = np.c_[X_norm, X1_squared, X2_squared, X1_X2_interaction]
intercept_term = np.c_[np.ones((X_poly.shape[0], 1)), X_poly]

XT = intercept_term.T
XTX = np.matmul(XT, intercept_term)
XTX_inv = np.linalg.inv(XTX)
XTy = np.matmul(XT, y)

betas = np.matmul(XTX_inv, XTy)
print(betas)

learning_rate = 0.00001 
iterations = 1000
m = X_poly.shape[0]

for i in range(iterations):
    y_pred = np.matmul(intercept_term, betas)
    error = y_pred - y
    gradients = (1/m) * (np.matmul(intercept_term.T, error))
    betas = betas - learning_rate * gradients

y_pred_gd = np.matmul(intercept_term, betas)


for i in range(10):
    actual = y[i]
    predicted = y_pred_gd[i]
    old = health_df["Predicted Readmission Rate"].iloc[i]
    print("Actual:", actual, "Predicted:", predicted, "Previous Prediction:", old)
