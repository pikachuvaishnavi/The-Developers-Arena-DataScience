# Sales Data Analysis Report

## Project Overview

This project analyzes a sales dataset using Python and the pandas library.  
The goal of the project is to explore sales data, clean the dataset, calculate important business metrics, and generate useful insights.

---

# Technologies Used

- Python
- Pandas

---

# Dataset Information

The dataset contains the following columns:

- Date
- Product
- Quantity
- Price
- Customer_ID
- Region
- Total_Sales

---

# Analysis Steps

## 1. Load Dataset

The CSV file was loaded using pandas.

```python
df = pd.read_csv("sales_data.csv")

## 2. Explore Dataset

The following details were checked:

Dataset shape
Column names
Data types
First 5 rows
 ## 3. Data Cleaning

The dataset was cleaned by:

Checking missing values
Removing duplicate records
df.isnull().sum()

df.drop_duplicates()
## 4. Sales Analysis

The following metrics were calculated:

Total Revenue
Best Selling Product
Total Quantity Sold
Average Sales
Highest Single Sale

Calculated Metrics
Metric	Description
Total Revenue ----	Total amount earned from sales
Best Selling Product ----	Product with highest revenue
Total Quantity Sold ----	Total items sold
Average Sales ----	Average revenue per sale
Highest Single Sale	----Maximum sale value

Insights
The dataset showed strong sales performance.
The best-selling product generated the highest revenue.
Average sales were consistent across transactions.
Data cleaning improved the accuracy of the analysis.
The report provides useful business insights for decision-making.

Sample Output
==================================================
           SALES ANALYSIS REPORT
==================================================

📌 Total Revenue        : ₹14,425,000.00
📌 Best Selling Product : Laptop
📌 Total Quantity Sold  : 520
📌 Average Sales        : ₹144,250.00
📌 Highest Single Sale  : ₹398,350.00

==================================================
                 INSIGHTS
==================================================

✅ Average sales are performing very well.
✅ Laptop is the top-performing product.
✅ The business generated strong overall revenue.

 Data analysis completed successfully!
==================================================
Conclusion

This project helped in understanding:

Data analysis using pandas
Loading and cleaning datasets
Calculating business metrics
Generating reports and insights
Basic Data Science workflow

The concepts learned in this project provide a strong foundation for future Data Science and Machine Learning projects.