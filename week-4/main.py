# E-commerce Sales Analysis Project
# Week 4 Internship Task

import pandas as pd
import matplotlib.pyplot as plt
import os

# Create directories for saving outputs
os.makedirs('visualizations', exist_ok=True)

# Load the dataset
try:
    df = pd.read_csv('data/sales_data.csv')
    print("Data loaded successfully! Here are the first 5 rows:")
    print(df.head())
except FileNotFoundError:
    print("Error: File not found. Please ensure 'sales_data.csv' is in the 'data/' folder.")

# Clean the data
# Drop any rows with missing values to prevent calculation errors
df.dropna(inplace=True)

# Convert the 'Date' column from text to datetime objects for time-based analysis [1]
df['Date'] = pd.to_datetime(df['Date'])

# 1. Total Sales by Product Category [1]
# Grouping by product and summing the Total_Sales column, sorted highest to lowest [1]
sales_by_product = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)
print("--- Total Sales by Product ---")
print(sales_by_product)

# 2. Total Sales by Region [1]
sales_by_region = df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)
print("\n--- Total Sales by Region ---")
print(sales_by_region)

# 3. Monthly Sales Trend (Bonus Analysis) [1]
# Extracting the month from the Date column to track pacing over time [1]
df['Month'] = df['Date'].dt.to_period('M')
sales_by_month = df.groupby('Month')['Total_Sales'].sum()
print("\n--- Total Sales by Month ---")
print(sales_by_month)


# Create a Bar Chart for Product Sales [1]
plt.figure(figsize=(10, 6))
sales_by_product.plot(kind='bar', color='#4C72B0', edgecolor='black')

# Add professional titles and labels
plt.title('Total Sales by Product Category', fontsize=14, fontweight='bold')
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Total Revenue ($)', fontsize=12)
plt.xticks(rotation=45) # Rotate labels so they don't overlap
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save and show
plt.tight_layout()
plt.savefig('visualizations/sales_by_product.png')
plt.show()


# Create a Pie Chart for Regional Sales Distribution [1]
plt.figure(figsize=(8, 8))

# Define distinct colors for the regions
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

# Create the pie chart, showing percentage values formatted to 1 decimal place
sales_by_region.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=colors, shadow=True)

# Professional formatting
plt.title('Revenue Distribution by Region', fontsize=14, fontweight='bold')
plt.ylabel('') # Hide the y-label as it's unnecessary for a pie chart

# Save and show
plt.tight_layout()
plt.savefig('visualizations/sales_by_region.png')
plt.show()

# Create a Line Chart for Monthly Trends [1]
plt.figure(figsize=(10, 6))

# Plot the monthly sales with markers at each data point
# Convert period index to string for cleaner plotting
sales_by_month.index = sales_by_month.index.astype(str) 
sales_by_month.plot(kind='line', marker='o', color='#2ca02c', linewidth=2, markersize=8)

# Add professional titles and labels
plt.title('Monthly Sales Trend (2024)', fontsize=14, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Revenue ($)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Save and show
plt.tight_layout()
plt.savefig('visualizations/monthly_sales_trend.png')
plt.show()


# ==========================================
# AUTOMATIC MARKDOWN REPORT GENERATOR
# ==========================================

import os

def generate_markdown_report(sales_by_product, sales_by_region, sales_by_month):

    # Create report folder automatically
    os.makedirs('report', exist_ok=True)

    # ==========================================
    # PRODUCT INSIGHTS
    # ==========================================

    top_product = sales_by_product.idxmax()
    top_product_sales = sales_by_product.max()

    bottom_product = sales_by_product.idxmin()
    bottom_product_sales = sales_by_product.min()

    # ==========================================
    # REGION INSIGHTS
    # ==========================================

    top_region = sales_by_region.idxmax()
    top_region_sales = sales_by_region.max()

    # ==========================================
    # MONTHLY INSIGHTS
    # ==========================================

    top_month = sales_by_month.idxmax()
    top_month_sales = sales_by_month.max()

    # Convert Period object to readable month
    top_month = str(top_month)

    # ==========================================
    # REPORT CONTENT
    # ==========================================

    report_content = f"""
# E-commerce Sales Analysis Report

## Executive Summary

This report analyzes sales transactions from the dataset to identify:
- Best-selling products
- Strongest sales regions
- Monthly sales trends

The project also includes visualizations using matplotlib.

---

# Key Insights & Patterns

## 1. Product Performance

- The best-selling product is **{top_product}**
- Total revenue generated: **${top_product_sales:,.2f}**

- The lowest-performing product is **{bottom_product}**
- Revenue generated: **${bottom_product_sales:,.2f}**

---

## 2. Regional Performance

- The top-performing region is **{top_region}**
- Revenue generated: **${top_region_sales:,.2f}**

This region contributes the highest percentage of total company revenue.

---

## 3. Monthly Sales Trend

- The highest sales month was **{top_month}**
- Monthly revenue: **${top_month_sales:,.2f}**

This indicates a strong sales period during the month.

---

# Charts Generated

The following visualizations were created:

## 1. Sales by Product

This bar chart shows total sales generated by each product category. 

![Sales by Product](../visualizations/sales_by_product.png)

## 2. Regional Sales Distribution

This pie chart shows revenue contribution from each region.

![Regional Sales](../visualizations/sales_by_region.png)

## 3. Monthly Sales Trend

This line chart shows how sales changed over time. 

![Monthly Sales Trend](../visualizations/monthly_sales_trend.png)

---

# Strategic Recommendations

- Focus marketing on high-performing products.
- Improve sales strategies for low-performing products.
- Expand successful strategies from the top region.
- Monitor monthly trends for better planning.

---

# Conclusion

This project demonstrates:
- Data loading and cleaning
- Data analysis using pandas
- Data visualization using matplotlib
- Insight generation
- Automated report creation

The project provides a complete beginner-friendly Data Science workflow.
"""

    # ==========================================
    # SAVE REPORT
    # ==========================================

    with open('report/analysis_report.md', 'w', encoding='utf-8') as file:
        file.write(report_content)

    print("\n✅ Report generated successfully!")
    print("📄 File saved as: report/analysis_report.md")


# ==========================================
# GENERATE REPORT
# ==========================================

generate_markdown_report(
    sales_by_product,
    sales_by_region,
    sales_by_month
)

