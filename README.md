# ISTA421_Exam2

Resource Link 1: https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2434813

Resource Link 2: https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/774388

Dataset Assessment: After assessing the data, it is clear to see that there are some problems in it. In the residual plot, there are some outliers and high leverage point seen, specifically where the residuals are at about -600, -420, and 320. The plotted data creates a funnel shape. This funnel shape is also seen in the linear regression model that uses number of discharges as a predictor for number of readmissions. This shape is also present in a linear regression model that uses the excess readmission ratio as a predictor for the number of readmissions. The funnel shape that is seen indicates non-constant variance of the error terms as well as some non-linearity. Multicollinearity is not present as the variance inflation factor (VIF) value for Number of Discharges and Expected Readmission Rate was about 1, and the VIF value for the Excess Readmission Ratio and Expected Readmission Rate was also about 1, meaning that these predictors are not correlated with one another. A Durbin Watson test was also created alongside the residual plot, and was used with Number of Discharges and Expected Remission Rate as predictors. The Durbin Watson test value is about 1.92, which is very close to 2 and indicates that there is no significantt correlation of error terms.

Variable description: 

**Facility Name** is a String that has the name of the medical center where the data was taken from.

**Facility ID** is an int that is a unique identifier for each medical center.

**State** is a String that has the abbreviation for each state that the medical center is in. All 50 states are present.

**Measure Name** is a String that provides information about the index to the quality and performance of a medical center in a certain procedure. 

**Number of Discharges** is a float that is the number of discharges that a medical center had in the given period of time.

**Footnote** is a float that is the number of additional notes regarding a certain data entry.

**Excess Readmission Ratio** is a float that is the ratio of actual readmission rates to expected readmission rates.

**Predicted Readmission Rate** is a float that is the predicted amount of patients to be readmitted.

**Expected Readmission Rate** is a float that is the expected amount of patients to be readmitted. 

**Number of Readmissions** is a float that is the number of actual readmissions.

**Start Date** is a String that has the start date of the collection of the data.

**End Date** is a String that has the end date of the collection of the data.


Research Question: How do the number of discharges and the expected readmission rate affect and predict the actual amount of patients who are readmitted?


Why research question would be interesting to the board: It would be interesting to the board as they are looking to better understand and better predict the amount of patients that get readmitted, in order to reduce costs. By creating a model that looks at the amount of people who are discharged from a medical center and the expected amount of patients to be readmitted, the factors influencing readmission rates can be better understood, and can give insignts into potential areas for improvement in the quality of care and discharge criteria, and ultimately, lower costs and spending for additional medical equipment and services.


Step 6 (Algorithm step): In this step, multivariate polynomial regression was implemented to predict the amount of readmissions. Generative AI was used in outlining the steps needed to complete a polynomial regression. Generative AI was also used to compute the gradient descent portion with this Google search being what my code is based off of. 

References:

Gradient Descent search:
https://www.google.com/search?q=gradient+descent+using+own+beta+values+python&rlz=1C1GEWG_enUS999US999&oq=gradient&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGDkyBggCEEUYOzIQCAMQABiRAhixAxiABBiKBTIMCAQQABhDGIAEGIoFMgwIBRAAGEMYgAQYigUyDQgGEAAYkQIYgAQYigUyDAgHEAAYQxiABBiKBTIMCAgQABhDGIAEGIoFMgwICRAAGEMYgAQYigXSAQgyMzQ3ajBqOagCALACAQ&sourceid=chrome&ie=UTF-8 

ChatGPT use: 
https://chatgpt.com/share/67fa8de2-c4f4-8004-993d-241f3003ac7a

VIF reference:
https://www.datacamp.com/tutorial/variance-inflation-factor


Instructions to run model:

For step_3_assessment.py, ensure that the FY_2025_Hospital_Readmissions_Reduction_Program_Hospital.csv file is downloaded and is in the same directory. Then, ensure that all packages and libraries are downloaded and run the code. 


For step_6_assessment.py, ensure that the FY_2025_Hospital_Readmissions_Reduction_Program_Hospital.csv file is downloaded and is in the same directory. Then, ensure that all packages and libraries are downloaded and run the code to view beta values, a sample of actual patients who were readmitted in comparison to the predicted values from the model and the predicted values from the dataset.


Findings:

From my model, the number of dischares and expected readmission rates predict the amount of patients who are readmitted fairly well, and indicates a strong relationship. From the sample that was output, most of the predictions made by my polynomial model are closer to the actual amount of patients discharged. There are a few times where this is not the case, as in one instance, the actual amount was 16, and my model predicted about *23 patients, while the  prediction from the dataset was about *16. However, one that stood out the most was an instance of where the actual was 95 patients, and the predicted value from the dataset was about *20. The polynomial regression model predicted that about *102 patients were going to be readmitted. While this prediction is 7 more than the actual, this will help allow medical centers to be more strategic in planning and allocated resources. As opposed to only expecting about 20 people being readmitted when the real amount is 4.75 times this. With these findings, discharge criteria should be reevaluated, and medical centers should ensure that they are not discharging people who are more at risk of coming back too hastily. Doing this will also increase quality of care and lead to saving on readmission costs. 

* Note that all decimal values were rounded up to the nearest whole number/person
