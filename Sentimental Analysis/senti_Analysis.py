# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
data = pd.read_csv("C:\\Users\\Teddy\\OneDrive\\Documents\\Oasis Intern\\Sentimental Analysis\\cleaned_reviews.csv")

# Data Exploration Steps
# Display the first 5 rows of the dataset
print(data.head())

# Display dataset information
print(data.info())

# Summary statistics of numerical features
print(data.describe()) #provides summary statistics.    


# checking missing values
print(data.isnull().sum())

# drop  missing values
data.dropna(inplace=True)


# drop duplicated values
data.drop_duplicates(inplace=True)
print(data.columns)

# Check the unique values in the sentiment column (if it exists)
print(data['Sentiment'].unique())