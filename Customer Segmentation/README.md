# Customer Segmentation Analysis

This project performs a customer segmentation analysis using a dataset from an e-commerce company. The goal is to segment customers based on their spending behavior and other relevant features. The analysis involves data exploration, feature engineering, and clustering using the K-Means algorithm. The results are visualized using various plots, including histograms, bar plots, and PCA-based scatter plots.

## Dataset

The dataset used in this project is from an e-commerce company. It contains information about customer spending on different product categories, their income, age, and marital status.

## Data Exploration

The initial steps involve exploring the dataset to understand its structure and content:

- Displaying the first few rows of the dataset
- Checking for missing values and duplicates
- Dropping unnecessary columns 
- Calculating key statistics like total spending and purchase frequency

## Feature Engineering

### Spending Segmentation

- **TotalSpent:** The total amount spent per customer across all product categories.
- **TotalPurchases:** The total number of purchases per customer across different channels.
- **SpendingSegment:** Customers are segmented into four categories (Low, Medium, High, Very High) based on their total spending.

## Clustering Analysis

The K-Means clustering algorithm is applied to the standardized features (`Income`, `MntTotal`, and `marital_Divorced`) to segment customers into distinct clusters.

- **Standardization:** Features are scaled to have a mean of 0 and a standard deviation of 1.
- **KMeans Clustering:** The algorithm is used to identify four clusters based on the selected features.

## Visualization

Several plots are created to visualize the data and the results of the clustering analysis:

- **Histograms:** For visualizing the distribution of `Age` and `Income`.
- **Bar Plot:** For showing the number of customers in each spending segment.
- **PCA Scatter Plot:** For visualizing the clusters in a 2D space using Principal Component Analysis (PCA).

## Conclusion

The project successfully segments customers based on their spending behavior, providing insights that can be used for targeted marketing strategies. The clustering analysis reveals distinct customer groups that could be further analyzed for business decision-making.

## Usage

To run the analysis, simply execute the Python script in your preferred environment. The visualizations will be displayed, and the results will be printed in the console.
