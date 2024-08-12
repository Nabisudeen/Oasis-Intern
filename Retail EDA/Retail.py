# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
data = pd.read_csv('C:\\Users\\Teddy\\OneDrive\\Documents\\Oasis Intern\\Retail EDA\\retail_sales_dataset.csv')


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
# calculating mean, median and standard deviation
mean_Quantity = data['Quantity'].mean()
median_Quantity = data['Quantity'].median()
std_Quantity = data['Quantity'].std()

print(f"Mean Quantity: {mean_Quantity}")
print(f"Median Quantity: {median_Quantity}")
print(f"Standard Deviation of Quantity: {std_Quantity}")

# convert date columns to datetime
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date',inplace=True)
print(data.head())

# Resample data to monthly frequency and sum sales
Monthly_sales = data['Total Amount'].resample('ME').sum()

# plot the monthly sales
plt.figure(figsize = (10, 6))
plt.plot(Monthly_sales, linestyle = '-')
plt.title('Monthly sales Trend', fontsize = 16)
plt.xlabel('Date', fontsize = 14)
plt.ylabel('Total sales', fontsize = 14)
plt.grid(True)
plt.show()

# plot the distribution of customer ages
plt.figure(figsize = (10, 6))
plt.hist(data['Age'], bins = 15, color ='skyblue', edgecolor = 'black', alpha = 0.7 )
plt.title('Customer Age Distribution', fontsize = 16)
plt.xlabel('Age', fontsize = 14)
plt.ylabel('Frequency', fontsize = 14)
plt.grid(False)
plt.show()

# plot the distribution of customer gender
Gender_count = data['Gender'].value_counts()

plt.figure(figsize=(10, 6))
plt.bar(Gender_count.index, Gender_count.values, color = 'blue', edgecolor = 'black', alpha = 0.7 )
plt.title('Customer Gender Distribution', fontsize = 16)
plt.xlabel('Gender', fontsize = 14)
plt.ylabel('Frequency', fontsize = 14)
plt.grid(False)
plt.show()

# plot the distribution of product categories
Product_count = data['Product Category'].value_counts()

plt.figure(figsize=(10, 6))
plt.bar(Product_count.index, Product_count.values, color = 'red', edgecolor = 'black', alpha = 0.7 )
plt.title('Product Category Distribution', fontsize = 16)
plt.xlabel('Product Category', fontsize = 14)
plt.ylabel('Frequency', fontsize = 14)
plt.grid(False)
plt.show()