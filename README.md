#### Group Members: Robert Huey, Eli Daniels, Luka Kelly

# Problem Statement:
_____________________________

This project aims to assist individuals in achieving their fitness goals by analyzing fitness activity through data from two distinct tracking devices, being Apple Watch vs Fitbit. Leveraging data from these devices, including health-related attributes, we will calculate BMI, combine user-specific insights and employ a predictive activity type model to create recommended fitness activities personalized to the individual to help them attain a BMI within the "normal" range.

# Notebook Outlines:
______________________________________
This notebook outline is comprised of two files and three notebooks. The data file contains all of the data we used for the project, which we pulled from https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/ZS2Z2J, as well as an additional dataset containing a list of exercises and respective calories burned per hour pulled from Kaggle (https://www.kaggle.com/datasets/aadhavvignesh/calories-burned-during-exercise-and-activities?resource=download).

The imports we used were:
+ pandas
+ matplotlib
+ seaborn 
+ dash
+ plotly
+ sklearn
+ numpy

The code file contains the three notebooks titled "01-Cleaning_EDA_preprocessing", "02-modeling", "03-Recommender". 

### 01-Cleaning_EDA_Preprocessing:
+ Load in the Datasets
    + Checked shape of dataframe and value counts of 'device' feature
    + We had no null values to drop
    + Dropped "Unnamed:0" column
+ Converting Weight and Height to Imperial Units
+ Using Height and Weight to Create BMI
+ Determining Device impact on health - calculating mean BMI in both Apple Watch and Fit Bit users
+ Calculating BMR
+ Generate graphs and interactive graphs

### 02-modeling:
+ Ran a K-Means Clustering Model to determine how the model would classify our known classifications of underweight, normal weight, overweight, and obese for optimized value of K. 
+ Ran a DBSCAN Model to compare the difference between the optimized value of K while comparing silhouette scores.
+ Ran a Random Forests Model to predict activity type for users based on their fitness and health data.     

### 03-Recommender:
+ Created a system that takes in several parameter inputs related to the user's characteristics and health metrics. Based on this information, it generates a list of recommended exercises tailored to the user's profile. The "Calories burned per hour for each exercise" portion of the code calculates and displays an estimate of the calories burned during various exercises based on the user's input weight. Based on these recommendations, we believe that this is the most optimal way for a user to achieve their health goals.


# Conclusions, and Recommendations
_______________________________
### Conclusions:

From our analysis and modeling, we can conclude that the K-Means Clustering Model and DBSCAN Model perform best with three clusters as compared to the four classes made by the CDC. These models however were not performing well due to the clusters not being clearly separated. This however was different from the random forest that we made that gave us an 88% accuracy score in predicting the activity type. Since our accuracy rate was high, we then took the activity types in question and created a recommender system to inform users what the best activity would be for them to reach their a healthy BMI. We also found that Apple Watch users have a higher average BMI than Fit Bit users. 

### Recommendations:

We would recommend that users do the activities recommended to them by our system to check to see if significant results were made towards moving their BMI to the desired range. If possible, it would be great to gather more data for different activities using these devices. 
