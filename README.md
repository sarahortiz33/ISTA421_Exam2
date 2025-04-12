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


Step 6 (Algorithm step):



Step 7 (Validation step):



Instructions to run model:

For step_3_assessment.py, ensure that the FY_2025_Hospital_Readmissions_Reduction_Program_Hospital.csv file is downloaded and is in the same directory. Then, ensure that all packages and libraries are downloaded and run the code. 


Findings:

