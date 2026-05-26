# Sales Data Analysis Project
# Week 3 Internship Task

# Import pandas library
import pandas as pd

# Load CSV file
df = pd.read_csv("sales_data.csv")

# Display first 5 rows
print("\n========== SAMPLE SALES DATA ==========\n")
print(df.head())

# Check dataset information
print("\n========== DATASET INFO ==========\n")
print("Shape of dataset:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

# Check missing values
print("\n========== MISSING VALUES ==========\n")
print(df.isnull().sum())

# Remove duplicates if any
df = df.drop_duplicates()

# Calculate Total Revenue
total_revenue = df['Total_Sales'].sum()

# Find Best Selling Product
best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()

# Find Total Quantity Sold
total_quantity = df['Quantity'].sum()

# Find Average Sales
average_sales = df['Total_Sales'].mean()

# Find Highest Sale
highest_sale = df['Total_Sales'].max()

# Generate Report
print("\n========== SALES REPORT ==========\n")

print(f"Total Revenue        : ₹{total_revenue:,.2f}")
print(f"Best Selling Product : {best_product}")
print(f"Total Quantity Sold  : {total_quantity}")
print(f"Average Sales        : ₹{average_sales:,.2f}")
print(f"Highest Single Sale  : ₹{highest_sale:,.2f}")

print("\n========== ANALYSIS COMPLETE ==========")

print("\n" + "=" * 50)
print("                 INSIGHTS")
print("=" * 50)

# Insights
if average_sales > 50000:  # Assuming 50,000 is a good average sales threshold
    print("✅ Average sales are performing very well.")
else:
    print("⚠️ Average sales are lower than expected.")

print(f"✅ {best_product} is the top-performing product.") #top performing product

if total_revenue > 100000:  # Assuming 100,000 is a good revenue threshold
    print("✅ The business generated strong overall revenue.")
else:
    print("⚠️ Revenue needs improvement.") 

print("\n  Data analysis completed successfully! ")
print("=" * 40)