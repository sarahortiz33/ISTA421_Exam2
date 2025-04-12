import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


health_df = pd.read_csv("FY_2025_Hospital_Readmissions_Reduction_Program_Hospital.csv")
    
health_df = health_df[health_df["Number of Readmissions"] != "Too Few to Report"]
health_df = health_df.dropna(subset=["Expected Readmission Rate", "Number of Readmissions", "Number of Discharges"])
health_df["Number of Readmissions"] = health_df["Number of Readmissions"].astype(int)


X = health_df[["Number of Discharges", "Expected Readmission Rate"]].values
y = health_df["Number of Readmissions"].values

XT = X.T
XTX = np.matmul(X, XT)
XTX_inv = np.linalg.inv(XTX)
XTy = np.matmul(XT, y)

betas = np.matmul(XTX_inv, XTy)
print(betas)
