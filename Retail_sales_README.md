# Retail Sales Data Analysis

## Project Overview

This project involves performing exploratory data analysis (EDA) on a retail sales dataset. The primary goal is to gain insights into the sales data, customer demographics, and product performance by applying various data processing and visualization techniques.

## Dataset

The dataset used in this project is a retail sales dataset that includes various attributes such as:
-Date: The date of the transaction.
-Quantity: The number of units sold.
-Total Amount: The total sales amount for the transaction.
-Age: The age of the customer.
-Gender: The gender of the customer.
-Product Category: The category of the product sold.

## Steps Performed

1. Data Loading:
   - The dataset is loaded using `pandas`.

2. Data Exploration:
   - Displayed the first few rows of the dataset using `head()`.
   - Obtained dataset information and summary statistics using `info()` and `describe()`.

3. Data Cleaning:
   - Checked for missing values and handled them by dropping rows with missing data.
   - Removed duplicated entries from the dataset.

4. Statistical Analysis:
   - Calculated the mean, median, and standard deviation for the `Quantity` column.

5. Data Preprocessing:
   - Converted the `Date` column to datetime format and set it as the index.

6. Data Resampling:
   - Resampled the data to a monthly frequency to analyze the sales trend.

7. Data Visualization:
   - Monthly Sales Trend: Plotted the monthly sales trend over time.
   - Customer Age Distribution: Visualized the distribution of customer ages.
   - Customer Gender Distribution: Plotted the distribution of customer genders.
   - Product Category Distribution: Visualized the distribution of product categories.

## Visualizations

The following visualizations were created to analyze the data:
1. Monthly Sales Trend: A line plot showing the trend of total sales on a monthly basis.
2. Customer Age Distribution: A histogram depicting the age distribution of customers.
3. Customer Gender Distribution: A bar chart showing the distribution of customers by gender.
4. Product Category Distribution: A bar chart illustrating the frequency of sales by product category.

## Conclusion

This analysis provides a comprehensive understanding of the retail sales data, including sales trends, customer demographics, and product performance. The insights derived from this project can help in making data-driven business decisions.

## Requirements

- Python 3.x
- Pandas
- Matplotlib

## How to Run

1. Ensure that the required libraries are installed.
2. Download or clone the repository.
3. Place the dataset (`retail_sales_dataset.csv`) in the appropriate directory.
4. Run the script to perform the analysis and generate visualizations.
