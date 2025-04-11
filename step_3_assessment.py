import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

health_df = pd.read_csv("healthcare-dataset-stroke-data.csv")

health_df.head()