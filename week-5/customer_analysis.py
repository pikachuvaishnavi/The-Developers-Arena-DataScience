# ==========================================
# CUSTOMER SALES ANALYSIS PROJECT
# Week 5 - Developers Arena Internship
# ==========================================
# Import pandas for data analysis
import pandas as pd

# Import matplotlib for creating charts
import matplotlib.pyplot as plt

# Import os for folder creation and file management
import os


# Create a folder named 'visualizations' if it doesn't already exist
os.makedirs("visualizations", exist_ok=True)


# ==========================================
# LOAD DATASETS
# ==========================================

try:
    # Load sales dataset
    sales_df = pd.read_csv("data/sales_data.csv")

    # Load customer churn dataset
    customer_df = pd.read_csv("data/customer_churn.csv")

    print("✅ Datasets Loaded Successfully!\n")

except FileNotFoundError:
    # Display error if dataset files are missing
    print("❌ Dataset file not found.")
    exit()


# ==========================================
# DATA EXPLORATION
# ==========================================

# Display first 5 rows of sales dataset
print("===== SALES DATA =====")
print(sales_df.head())

# Display first 5 rows of customer dataset
print("\n===== CUSTOMER DATA =====")
print(customer_df.head())

# Show column names, data types, and null values
print("\n===== SALES DATA INFO =====")
print(sales_df.info())

print("\n===== CUSTOMER DATA INFO =====")
print(customer_df.info())


# ==========================================
# DATA CLEANING
# ==========================================

# Remove rows containing missing values
sales_df.dropna(inplace=True)
customer_df.dropna(inplace=True)

# Remove duplicate rows
sales_df.drop_duplicates(inplace=True)
customer_df.drop_duplicates(inplace=True)


# ==========================================
# DATE HANDLING
# ==========================================

# Convert Date column to datetime format
sales_df["Date"] = pd.to_datetime(sales_df["Date"])

# Extract year from Date column
sales_df["Year"] = sales_df["Date"].dt.year

# Extract month from Date column
sales_df["Month"] = sales_df["Date"].dt.month

# Extract day from Date column
sales_df["Day"] = sales_df["Date"].dt.day


# ==========================================
# STRING OPERATIONS
# ==========================================

# Convert product names to uppercase for consistency
sales_df["Product"] = sales_df["Product"].str.upper()


# ==========================================
# FILTERING DATA
# ==========================================

# Find sales greater than 500 from East region
high_sales = sales_df[
    (sales_df["Total_Sales"] > 500)
    & (sales_df["Region"] == "East")
]

print("\n===== HIGH SALES IN EAST REGION =====")
print(high_sales.head())

# Find records belonging to East OR West region
east_west_sales = sales_df[
    (sales_df["Region"] == "East")
    | (sales_df["Region"] == "West")
]


# ==========================================
# AGGREGATION 1 - MONTHLY SALES
# ==========================================

# Calculate total sales for each month
monthly_sales = sales_df.groupby("Month")["Total_Sales"].sum()

print("\n===== MONTHLY SALES =====")
print(monthly_sales)


# ==========================================
# AGGREGATION 2 - PRODUCT SALES
# ==========================================

# Calculate total sales for each product
product_sales = sales_df.groupby("Product")["Total_Sales"].sum()

print("\n===== PRODUCT SALES =====")
print(product_sales)


# ==========================================
# AGGREGATION 3 - REGION SALES
# ==========================================

# Calculate total sales for each region
region_sales = sales_df.groupby("Region")["Total_Sales"].sum()

print("\n===== REGION SALES =====")
print(region_sales)


# ==========================================
# TOP CUSTOMERS
# ==========================================

# Calculate customer revenue and sort descending
top_customers = (
    sales_df.groupby("Customer_ID")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== TOP 5 CUSTOMERS =====")
print(top_customers.head())


# ==========================================
# MERGE DATASETS
# ==========================================

# Rename CustomerID column if necessary
if "CustomerID" in customer_df.columns:
    customer_df.rename(
        columns={"CustomerID": "Customer_ID"},
        inplace=True
    )

try:
    # Merge sales and customer datasets using Customer_ID
    merged_df = pd.merge(
        sales_df,
        customer_df,
        on="Customer_ID",
        how="inner"
    )

    print("\n===== MERGED DATA =====")
    print(merged_df.head())

except:
    print("\n⚠ Merge could not be completed because IDs do not match.")


# ==========================================
# PIVOT TABLE
# ==========================================

# Create pivot table showing sales by region and product
pivot_table = pd.pivot_table(
    sales_df,
    values="Total_Sales",
    index="Region",
    columns="Product",
    aggfunc="sum",
    fill_value=0
)

print("\n===== PIVOT TABLE =====")
print(pivot_table)


# ==========================================
# BUSINESS METRICS
# ==========================================

# Calculate total company revenue
total_revenue = sales_df["Total_Sales"].sum()

# Count unique customers
total_customers = sales_df["Customer_ID"].nunique()

# Calculate average order value
average_order_value = sales_df["Total_Sales"].mean()

# Identify best-selling product
best_product = product_sales.idxmax()

# Identify top-performing region
best_region = region_sales.idxmax()

# Identify highest-spending customer
top_customer = top_customers.idxmax()

# Revenue generated by top customer
top_customer_sales = top_customers.max()


# ==========================================
# VISUALIZATION 1 - BAR CHART
# ==========================================

# Create figure size
plt.figure(figsize=(8, 5))

# Plot product sales bar chart
product_sales.plot(kind="bar")

# Chart title and labels
plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Revenue")

# Adjust spacing
plt.tight_layout()

# Save chart image
plt.savefig("visualizations/product_sales.png")

# Display chart
plt.show()

# ==========================================
# VISUALIZATION 2
# MONTHLY SALES LINE CHART
# ==========================================

plt.figure(figsize=(8, 5))

monthly_sales.plot(
    kind="line",
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig(
    "visualizations/monthly_sales.png"
)

plt.show()

# ==========================================
# VISUALIZATION 3
# REGION SALES PIE CHART
# ==========================================

plt.figure(figsize=(8, 8))

region_sales.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")

plt.title("Regional Sales Distribution")

plt.savefig(
    "visualizations/region_sales.png"
)

plt.show()

# ==========================================
# VISUALIZATION 4
# CUSTOMER CHURN CHART
# ==========================================

if "Churn" in customer_df.columns:

    plt.figure(figsize=(8, 8))

    customer_df["Churn"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.title("Customer Churn Distribution")
    plt.ylabel("")

    plt.savefig(
        "visualizations/churn_distribution.png"
    )

    plt.show()

# ==========================================
# GENERATE ANALYSIS REPORT
# ==========================================

top_product = product_sales.idxmax()
top_product_sales = product_sales.max()

bottom_product = product_sales.idxmin()
bottom_product_sales = product_sales.min()

top_region = region_sales.idxmax()
top_region_sales = region_sales.max()

top_month = monthly_sales.idxmax()
top_month_sales = monthly_sales.max()

report = f"""
# Customer Sales Analysis Report

## Executive Summary

This report analyzes customer sales and purchasing patterns from the dataset to identify:

- Top-performing customers
- Best-selling products
- Strongest sales regions
- Monthly sales trends
- Customer retention insights

The project also includes data visualizations created using matplotlib and advanced analysis using pandas.

---

# Key Insights & Patterns

-Total Revenue generated: ${total_revenue:,.2f}

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

This indicates a strong sales period during that month.

---

## 4. Customer Analysis

- Total Customers: **{total_customers}**
- Average Order Value: **${average_order_value:,.2f}**

- Top Customer: **{top_customer}**
- Customer Revenue: **${top_customer_sales:,.2f}**

The top customer contributes significantly to overall business revenue.

---

# Charts Generated

The following visualizations were created:

## 1. Product Sales Analysis

This bar chart compares total revenue generated by each product category.

![Product Sales](visualizations/product_sales.png)

---

## 2. Monthly Sales Trend

This line chart shows how revenue changes across different months.

![Monthly Sales Trend](visualizations/monthly_sales.png)

---

## 3. Regional Sales Distribution

This pie chart shows the revenue contribution from each region.

![Regional Sales Distribution](visualizations/region_sales.png)

---

## 4. Customer Churn Distribution

This pie chart visualizes customer retention and churn behavior.

![Customer Churn Distribution](visualizations/churn_distribution.png)

---

# Strategic Recommendations

## Business Recommendations

### 1. Focus on Top-Performing Products

The **{top_product}** category generated the highest revenue (**${top_product_sales:,.2f}**), making it the company's strongest product line. Increasing inventory availability, promotional campaigns, and product bundles can further boost revenue.

### 2. Improve Customer Retention Strategies

The top customer (**{top_customer}**) generated **${top_customer_sales:,.2f}** in revenue, showing that loyal customers contribute significantly to business growth. Implementing loyalty programs, personalized offers, and customer engagement initiatives can help retain valuable customers and increase repeat purchases.

### 3. Expand Marketing in Strong-Performing Regions

The **{top_region}** region generated the highest revenue (**${top_region_sales:,.2f}**). Investing more in marketing campaigns, regional partnerships, and customer acquisition efforts in this region can maximize sales opportunities and strengthen market presence.

### 4. Improve Performance of Low-Selling Products

The **{bottom_product}** category generated the lowest revenue (**${bottom_product_sales:,.2f}**). Discount offers, product bundles, and targeted promotions may help increase demand and improve sales performance.

### 5. Leverage Monthly Sales Trends

Sales peaked during month **{top_month}**, generating **${top_month_sales:,.2f}** in revenue. Understanding the factors behind this strong performance can help the company replicate successful strategies during slower sales periods.

---

By focusing on high-performing products, retaining valuable customers, and strengthening successful regions, the company can improve overall revenue growth and long-term customer satisfaction.

---

# Conclusion

This project demonstrates:

- Data loading and cleaning
- Data transformation using pandas
- Grouping and aggregation operations
- Data filtering with multiple conditions
- Datetime handling
- Pivot table creation
- Data visualization using matplotlib
- Customer purchasing pattern analysis
- Automated report generation

The project provides a complete intermediate-level Data Science workflow and valuable business insights for decision-making.
"""

with open(
    "analysis_report.md",
    "w",
    encoding="utf-8"
) as file:
    file.write(report)

print("\\n✅ Analysis Report Generated Successfully!")
print("📄 File saved as: analysis_report.md")
