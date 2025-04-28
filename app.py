import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for plots
#plt.style.use('seaborn-whitegrid')
sns.set_palette("colorblind")

# Load the dataset
# Assuming the data is in a CSV file named "property_sales.csv"
df = pd.read_csv("/content/propertydataset.csv")

# Display basic information about the dataset
print("Dataset Shape:", df.shape)
print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

print("\nCheck for missing values:")
print(df.isnull().sum())

# Convert date columns to datetime
df['Date Recorded'] = pd.to_datetime(df['Date Recorded'], format='%d-%m-%Y', errors='coerce') # Added format and errors argument
# Extract year and month from the date
df['Year'] = df['Date Recorded'].dt.year
df['Month'] = df['Date Recorded'].dt.month

# Data Analysis
# 1. Distribution of Sale Amounts
plt.figure(figsize=(10, 6))
sns.histplot(df['Sale Amount'], kde=True)
plt.title('Distribution of Sale Amounts')
plt.xlabel('Sale Amount')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('sale_amount_distribution.png')
plt.close()

# 2. Sales by Property Type
plt.figure(figsize=(12, 6))
sales_by_type = df.groupby('Property Type')['Sale Amount'].mean().sort_values(ascending=False)
sns.barplot(x=sales_by_type.index, y=sales_by_type.values)
plt.title('Average Sale Amount by Property Type')
plt.xlabel('Property Type')
plt.ylabel('Average Sale Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_by_property_type.png')
plt.close()

# 3. Sales Ratio Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Sales Ratio'], kde=True)
plt.title('Distribution of Sales Ratio')
plt.xlabel('Sales Ratio')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('sales_ratio_distribution.png')
plt.close()

# 4. Correlation between Assessed Value and Sale Amount
plt.figure(figsize=(8, 8))
sns.scatterplot(x='Assessed Value', y='Sale Amount', data=df, alpha=0.6)
plt.title('Assessed Value vs Sale Amount')
plt.xlabel('Assessed Value')
plt.ylabel('Sale Amount')
plt.tight_layout()
plt.savefig('assessed_vs_sale.png')
plt.close()

# 5. Sales Trends Over Time (if data spans multiple years)
plt.figure(figsize=(12, 6))
monthly_sales = df.groupby(['Year', 'Month'])['Sale Amount'].mean().reset_index()
sns.lineplot(x='Month', y='Sale Amount', hue='Year', data=monthly_sales)
plt.title('Average Sale Amount Trends by Month and Year')
plt.xlabel('Month')
plt.ylabel('Average Sale Amount')
plt.tight_layout()
plt.savefig('sales_trends.png')
plt.close()

# 6. Sales Amount by Town
plt.figure(figsize=(14, 8))
town_sales = df.groupby('Town')['Sale Amount'].mean().sort_values(ascending=False).head(15)
sns.barplot(x=town_sales.index, y=town_sales.values)
plt.title('Average Sale Amount by Town (Top 15)')
plt.xlabel('Town')
plt.ylabel('Average Sale Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_by_town.png')
plt.close()

# 7. Residential Type Analysis (if applicable)
if 'Residential Type' in df.columns and not df['Residential Type'].isnull().all():
    plt.figure(figsize=(12, 6))
    res_type_sales = df.groupby('Residential Type')['Sale Amount'].mean().sort_values(ascending=False)
    sns.barplot(x=res_type_sales.index, y=res_type_sales.values)
    plt.title('Average Sale Amount by Residential Type')
    plt.xlabel('Residential Type')
    plt.ylabel('Average Sale Amount')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('sales_by_residential_type.png')
    plt.close()

# 8. Heatmap of correlations between numerical variables
plt.figure(figsize=(10, 8))
numeric_df = df.select_dtypes(include=[np.number])
correlation = numeric_df.corr()
mask = np.triu(correlation)
sns.heatmap(correlation, annot=True, cmap='coolwarm', mask=mask)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
plt.close()

# 9. Box plot of Sale Amount by Property Type
plt.figure(figsize=(14, 8))
sns.boxplot(x='Property Type', y='Sale Amount', data=df)
plt.title('Sale Amount Distribution by Property Type')
plt.xlabel('Property Type')
plt.ylabel('Sale Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('boxplot_sale_by_property.png')
plt.close()

# 10. Sale Amount to Assessed Value Ratio by Town
plt.figure(figsize=(14, 8))
df['Value_Ratio'] = df['Sale Amount'] / df['Assessed Value']
town_value_ratio = df.groupby('Town')['Value_Ratio'].mean().sort_values(ascending=False).head(15)
sns.barplot(x=town_value_ratio.index, y=town_value_ratio.values)
plt.title('Average Sale/Assessed Value Ratio by Town (Top 15)')
plt.xlabel('Town')
plt.ylabel('Sale Amount / Assessed Value')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('value_ratio_by_town.png')
plt.close()

# Display summary of findings
print("\n--- Summary of Key Findings ---")
print(f"Total records: {len(df)}")
print(f"Date range: {df['Date Recorded'].min()} to {df['Date Recorded'].max()}")
print(f"Average Sale Amount: ${df['Sale Amount'].mean():,.2f}")
print(f"Median Sale Amount: ${df['Sale Amount'].median():,.2f}")
print(f"Average Sales Ratio: {df['Sales Ratio'].mean():.4f}")
print(f"Most common property type: {df['Property Type'].value_counts().idxmax()}")
print(f"Town with highest average sale price: {town_sales.idxmax()} (${town_sales.max():,.2f})")
print(f"Correlation between Assessed Value and Sale Amount: {df['Assessed Value'].corr(df['Sale Amount']):.4f}")