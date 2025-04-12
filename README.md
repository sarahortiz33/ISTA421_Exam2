# ISTA421_Exam2

Resource Link 1: https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2434813

Resource Link 2: https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/774388

Dataset Assessment: After assessing the data, it is clear to see that there are some problems in it. In the residual plot, there are some outliers and high leverage point seen, and the data creates a funnel shape. This funnel shape is also seen in the linear regression model that uses number of discharges as a predictor for number of readmissions. This shape is also present in a linear regression model that uses the excess readmission ratio as a predictor for the number of readmissions. The funnel shape that is seen indicates non-constant variance of the error terms. 

# No multicollinearity is present
# An additional Durbin Watson test alongside the residual and fitted value plot indicates no correlation of error terms
# A few high leverage points are present. The most notable ones being at about -600, -420, 320
# Non linearity 





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


Research Question:



Why research question would be interesting to the board: 



Step 6 (Algorithm step):



Step 7 (Validation step):



Instructions to run model:


Findings:

