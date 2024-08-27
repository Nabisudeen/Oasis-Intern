# importing necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Loading dataset
Data = pd.read_csv(r'C:\Users\Teddy\OneDrive\Documents\Oasis Intern\Customer Segmentation\ifood_df.csv')

# Data Exploration Steps
# Display the first 5 rows of the dataset
print(Data.head())

# Display dataset information
print(Data.info())

# Summary statistics of numerical features
print(Data.describe()) #provides summary statistics.    


# checking missing values
print(Data.isnull().sum())

# drop  missing values
Data.dropna(inplace=True)

# drop duplicates
Data.drop(columns=['Z_CostContact','Z_Revenue'],inplace=True)
Data.drop_duplicates(inplace=True)
print(Data.columns)

# Calculate the total amount spent per customer
Data['TotalSpent'] = (Data['MntWines'] + Data['MntFruits'] + Data['MntMeatProducts'] + Data['MntFishProducts'] + Data['MntSweetProducts'] + Data['MntGoldProds'] )
# calculate average purchase values
avg_purchase_value = Data['TotalSpent'].mean()
print("Average Purchase Values :", avg_purchase_value)

# Calculate the total number of purchases per customer
Data['TotalPurchases'] = (Data['NumDealsPurchases'] + Data['NumWebPurchases'] + Data['NumCatalogPurchases'] + Data['NumStorePurchases'])
# Calculate average frequency of puchase
avg_purchase_Freq = Data['TotalPurchases'].mean()
print("Average Purchase Frequency :", avg_purchase_Freq)

# Median Purchase Value
median_purchase_value = Data['TotalSpent'].median()
print("Median Purchase Value :",median_purchase_value)

# Total Revenue
total_revenue = Data['TotalSpent'].sum()
print("Total Revenue :",total_revenue)

# Summary statistics for total amount spent and total purchases
print(Data[['TotalSpent', 'TotalPurchases']].describe())

# Define spending segments based on quantiles
Data['SpendingSegment'] = pd.qcut(Data['TotalSpent'], q=4, labels=['Low', 'Medium', 'High', 'Very High'])

# Display the first few rows with spending segments
print(Data[['TotalSpent', 'SpendingSegment']].head())

# Count the number of customers in each segment
spending_segment_counts = Data['SpendingSegment'].value_counts()
print(spending_segment_counts)

# Bar plot of the number of customers in each spending segment
plt.figure(figsize=(10, 6))
sns.countplot(x='SpendingSegment', data=Data, palette='pastel')
plt.title('Number of Customers in Each Spending Segment')
plt.xlabel('Spending Segment')
plt.ylabel('Number of Customers')
plt.show()

# histogram for age
plt.figure(figsize=(8, 6))  
sns.histplot(data=Data, x='Age', bins=30)
plt.title('Histogram for Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# histogram for income
plt.figure(figsize=(8, 6))  
sns.histplot(data=Data, x='Income', bins=30)
plt.title('Histogram for Income')
plt.xlabel('Income')
plt.ylabel('Frequency')
plt.show()

# Standardising data
scaler = StandardScaler()
cols_for_clustering = ['Income', 'MntTotal', 'marital_Divorced']
Data_scaled = Data.copy()
Data_scaled[cols_for_clustering] = scaler.fit_transform(Data[cols_for_clustering])
print(Data_scaled[cols_for_clustering].describe())

# Perform KMeans clustering 
kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
Data['Cluster'] = kmeans.fit_predict(Data_scaled[cols_for_clustering])

# Cluster Distribution in Principal Component Space(Analysis)
pca = PCA(n_components=2)
Data_pca = pca.fit_transform(Data_scaled[cols_for_clustering])
Data['PCA1'] = Data_pca[:, 0]
Data['PCA2'] = Data_pca[:, 1]

plt.figure(figsize=(10, 6))
sns.scatterplot(x='PCA1', y='PCA2', hue='Cluster', data=Data, palette='viridis')
plt.title('Clusters Visualized in 2D PCA Space')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.show()