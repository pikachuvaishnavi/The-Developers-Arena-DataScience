# Customer Sales Analysis Project

## Week 5 – Advanced Data Manipulation with Pandas

### Project Overview

This project analyzes customer sales data and customer churn data using Python, Pandas, and Matplotlib.

The objective is to understand customer purchasing behavior, identify top-performing products and regions, analyze sales trends, and generate business insights through data analysis and visualization.

---

## Project Objectives

* Load and explore sales and customer datasets
* Clean and preprocess data
* Perform grouping and aggregation operations
* Filter data using multiple conditions
* Extract date components from datetime data
* Merge multiple datasets
* Create pivot tables for summarization
* Generate visualizations using Matplotlib
* Create an automated analysis report

---

## Technologies Used

* Python 3.x
* Pandas
* Matplotlib

---

## Project Structure

```text
week-5/
│
├── data/
│   ├── sales_data.csv
│   └── customer_churn.csv
│
├── screenshots/
│
├── visualizations/
│   ├── product_sales.png
│   ├── monthly_sales.png
│   ├── region_sales.png
│   └── churn_distribution.png
│
├── customer_analysis.py
├── analysis_report.md
├── requirements.txt
└── README.md
```

---

## Installation & Setup

### Step 1: Clone the Repository

```bash
git clone <repository-url>
```

### Step 2: Navigate to Project Folder

```bash
cd week-5
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Project

```bash
python customer_analysis.py
```

---

## Dataset Information

### sales_data.csv

Contains sales transaction records.

Typical Columns:

* Customer_ID
* Product
* Region
* Date
* Total_Sales

### customer_churn.csv

Contains customer retention information.

Typical Columns:

* Customer_ID
* Customer Name
* Region
* Churn

---

## Features Implemented

### Data Cleaning

* Removed missing values
* Removed duplicate records

### Date Handling

* Converted Date column to datetime format
* Extracted Year, Month, and Day

### String Operations

* Converted product names to uppercase

### Filtering

* High sales transactions in East region
* Regional filtering using AND and OR conditions

### Aggregations

* Monthly Sales Analysis
* Product Sales Analysis
* Regional Sales Analysis

### Customer Analysis

* Top customers by revenue
* Total customers
* Average order value

### Data Merging

* Combined customer and sales datasets using Customer_ID

### Pivot Tables

* Product sales across regions

### Data Visualization

* Product Sales Bar Chart
* Monthly Sales Trend Line Chart
* Regional Sales Pie Chart
* Customer Churn Distribution Pie Chart

### Report Generation

Automatically generates:

```text
analysis_report.md
```

with:

* Executive Summary
* Key Insights
* Business Metrics
* Charts
* Strategic Recommendations
* Conclusion

---

## Key Business Metrics

The project calculates:

* Total Revenue
* Total Customers
* Average Order Value
* Best Selling Product
* Top Performing Region
* Top Customer
* Monthly Sales Trends

---

## Visualizations Generated

### Product Sales Analysis

Bar chart showing revenue by product.

### Monthly Sales Trend

Line chart showing sales growth over time.

### Regional Sales Distribution

Pie chart showing revenue contribution by region.

### Customer Churn Distribution

Pie chart showing retained vs churned customers.

---

## Learning Outcomes

Through this project, I learned:

* Advanced Pandas operations
* Data grouping and aggregation
* Data filtering techniques
* Data merging and joining
* Pivot table creation
* Datetime processing
* Data visualization with Matplotlib
* Business insight generation
* Automated report generation

---

## Author

**Vaishnavi**

Developers Arena Internship – Week 5 Project
