# 🚀 Customer Lifetime Value Prediction System

## 📌 Overview

This project focuses on predicting customer spending over a future 90-day period using historical purchasing behavior. Using the Online Retail dataset, I performed data cleaning, exploratory data analysis (EDA), feature engineering, model training, and hyperparameter optimization to build a Customer Lifetime Value (CLV) prediction model. The final tuned Random Forest model was saved using Joblib and integrated into a Streamlit application for CLV predictions.

-----

## 🤔 Problem Statement & Business Impact

E-commerce businesses need to predict how much customers will spend in the next 90 days to make better decisions about marketing, retention, and sales planning. This project uses historical purchase data to predict future customer spending.

- **Customer Retention:** Identify customers who may need extra attention.
- **Marketing Optimization:** Focus marketing efforts on high-value customers.
- **Revenue Planning:** Better estimate future customer spending.
- **Customer Segmentation:** Group customers by predicted value.
- **Data-Driven Decisions:** Make smarter business decisions using customer data.

-----

## 📂 Project Structure

```text
Customer Lifetime Value Prediction System
│
├── data
│   ├── cleaned_data.csv
│   ├── final_data.csv
│   └── OnlineRetail.csv
│
├── images                 # EDA charts and visualizations
│
├── models                   # Saved machine learning model
│   ├── customer_lifetime_value_columns.pkl
│   └── customer_lifetime_value_model.pkl
│
├── notebooks              # Jupyter notebooks for analysis
│   ├── 1. EDA & Data Cleaning.ipynb
│   ├── 2. Feature Engineering.ipynb
│   └── 3. Model Training & Evaluation.ipynb
│
├── .gitignore
├── app.py                   # Streamlit application
├── LICENSE
├── README.md
└── requirements.txt
```

-----

## 📈 Dataset 

[Original Online Retail Dataset — Kaggle](https://www.kaggle.com/datasets/vijayuv/onlineretail)

- **Original Dataset Columns:** ['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country']
- **Original Dataset Overview:** The data has 541909 rows, 8 columns and it does not have important features like recency, frequency, monetary and clv.
- **Prepared Dataset Columns:** ['Recency', 'Frequency', 'Monetary', 'CLV', 'TotalQuantity', 'UniqueProducts', 'ActiveDays', 'CustomerTenureDays', 'AverageUnitPrice', 'AverageQuantity', 'AverageTransactionValue', 'UniqueCountries']
- **Prepared Dataset Overview:** The data has 3370 rows and 12 columns

-----

## 🔍 Some Interesting Prepared Feature Overview 

- **Recency:** How many days since the customer’s last purchase
- **Frequency:** How many different orders the customer made
- **Monetary:** Total money spent by the customer
- **CLV:** Total amount the customer spends during the 90-day period.

-----

## 🛠️ Tech Stack

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Optuna
- Joblib
- Streamlit
- Jupyter Notebook

-----

## 🚀 How to Run the Application Locally

Follow these steps to run the application on your local system.

### 1. Clone the Repository

```bash
git clone https://github.com/curious-arin/Customer-Lifetime-Value-Prediction-System.git

cd Customer-Lifetime-Value-Prediction-System
```

### 2. Create and Activate a Virtual Environment

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on **Windows PowerShell**:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Ensure that Python 3.12 is installed. Install the required libraries using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

From the repository directory, run the following command:

```bash
streamlit run app.py
```

The application will open in your default web browser. If it does not open automatically, visit the local URL displayed in your terminal, usually `http://localhost:8501`.

-----

## 🔄 Project Workflow

1. **Data Loading & Understanding**
   - Loaded the Online Retail dataset containing 541,909 transactions.
   - Examined data types, missing values, duplicate records, and dataset structure.

2. **Data Cleaning & Preprocessing**
   - Identified cancelled invoices.
   - Removed transactions with missing `CustomerID`.
   - Removed the `IsCancelled` column from the cleaned dataset.
   - Handled missing product descriptions.
   - Created `TotalPrice = Quantity × UnitPrice`.

3. **Exploratory Data Analysis (EDA)**
   - Analyzed revenue trends over time.
   - Identified top products by revenue and quantity sold.
   - Examined revenue by country, month, and weekday.
   - Identified high-revenue customers.
   - Compared repeat and one-time customers.
   - Investigated numerical feature correlations.

4. **Feature Engineering**
   - Created customer-level RFM features:
     - `Recency`: Days since the customer's last purchase
     - `Frequency`: Number of unique invoices.
     - `Monetary`: Total historical spending.
   - Engineered additional features, including total quantity, unique products, active days, customer tenure, average unit price, average quantity, average transaction value, and unique countries.

5. **Target Variable Creation**
   - Used a time-based split to separate historical transactions from the final 90-day future period.
   - Calculated each customer's spending during the future period as `CLV`.
   - Assigned a CLV of zero to customers with no purchases during that period.
   - Merged the target with historical customer features.

6. **Data Preprocessing**
   - Split the engineered dataset into training and testing sets.
   - Applied `log1p` transformation and standard scaling to input features through a preprocessing pipeline.
   - Applied a log transformation to the target variable using `TransformedTargetRegressor`, with inverse transformation for predictions.

7. **Model Training & Comparison**
   - Trained and compared five regression algorithms:
     - Linear Regression
     - K-Nearest Neighbors (KNN)
     - Decision Tree
     - Random Forest
     - XGBoost

8. **Hyperparameter Optimization**
   - Used Optuna with a TPE sampler for Bayesian-search-based optimization.
   - Evaluated candidate models using cross-validation MAE.
   - Selected a tuned Random Forest model for the final implementation.

9. **Model Evaluation**
   - Evaluated the final model using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R².
   - Compared training and testing performance to examine overfitting.

10. **Model Saving & Deployment**
    - Saved the trained model and feature-column names using Joblib.
    - Built a Streamlit interface for entering customer information and generating estimated 90-day CLV predictions.

-----

## 📊 Exploratory Data Analysis

### 1. What is the distribution of cancelled invoices?
- **The dataset contains 9,288 cancelled invoices.**
<img src="https://github.com/curious-arin/Customer-Lifetime-Value-Prediction-System/blob/main/images/1.cancelled_invoices.png" width="100%">


### 2. Total Revenue Overtime
- **Revenue remains relatively stable until getting a massive spike**
<img src="https://github.com/curious-arin/Customer-Lifetime-Value-Prediction-System/blob/main/images/2.total_revenue_over_time.png" width="100%">


### 3. Top 10 countries by revenue
- **United Kingdom generates the highest revenue**
<img src="https://github.com/curious-arin/Customer-Lifetime-Value-Prediction-System/blob/main/images/3.top_10_revenue_countries.png" width="100%">


### 4. Top 10 products by revenue
- **The paper craft little birdie generates the highest revenue.**
<img src="https://github.com/curious-arin/Customer-Lifetime-Value-Prediction-System/blob/main/images/4.top_products_by_revenue.png" width="100%">


### 5. Top 10 products by quantity sold
- **PAPER CRAFT , LITTLE BIRDIE and MEDIUM CERAMIC TOP STORAGE JAR are sold the most.**
<img src="https://github.com/curious-arin/Customer-Lifetime-Value-Prediction-System/blob/main/images/5.top_products_by_quantity_sold.png" width="100%">
 

### 6. Monthly Revenue
- **Overall monthly revenue steadily increases before peaking in November.**
<img src="https://github.com/curious-arin/Customer-Lifetime-Value-Prediction-System/blob/main/images/6.monthly_revenue.png" width="100%">


### 7. Revenue Share by Weekday
- **Thursday and Tuesday generate the largest shares of revenue**
<img src="https://github.com/curious-arin/Customer-Lifetime-Value-Prediction-System/blob/main/images/7.revenue_share_by_weekday.png" width="100%">


### 8. Items per rder
- **Order quantities are usually low but feature extreme outliers.**
<img src="https://github.com/curious-arin/Customer-Lifetime-Value-Prediction-System/blob/main/images/8.items_per_order.png" width="100%">


### 9. Top 10 Customers by Revenue
- **Customer with CustomerID (14646.0) is the top customer that generates the highest revenue in the analysis.**
<img src="https://github.com/curious-arin/Customer-Lifetime-Value-Prediction-System/blob/main/images/9.customers_by_revenue.png" width="100%">


### 10. Repeat vs One-time Customers
- **The data shows 65.6% Repeat customers and 34.4% One time customers.**
<img src="https://github.com/curious-arin/Customer-Lifetime-Value-Prediction-System/blob/main/images/10.repeat_vs_onetime_customers.png" width="100%">


### 11. Correlation Heatmap Before Feature Engineering
- **The plot shows a strong positive correlation of 0.91 between Quantity and TotalPrice, with other features showing near zero correlation to each other.**
<img src="https://github.com/curious-arin/Customer-Lifetime-Value-Prediction-System/blob/main/images/11.correlation_heatmap_before_feature_engineering.png" width="100%">


### 12. Skewness Distribution Before Feature Engineering
* **Data is right skewed, i will later decide what better can be done**
<img src="https://github.com/curious-arin/Customer-Lifetime-Value-Prediction-System/blob/main/images/12.skewed_distributions.png" width="100%">


### 13. Distribution of Customer Lifetime Value
- **The customer lifetime value distribution is highly right-skewed, showing that the majority of customers generate low value, leaving few high value outliers.**
<img src="https://github.com/curious-arin/Customer-Lifetime-Value-Prediction-System/blob/main/images/13.clv_distribution.png" width="100%">


### 14. Correlation Heatmap After Feature Engineering
- **TotalQuantity has the strongest positive correlation with CLV at 0.76 & Monetary value at 0.65, indicating that higher purchase volume and spending strongly predict customer lifetime value. Because many features showed limited correlation, new features and a target variable was engineered, and the dataset is now prepared for model training**
<img src="https://github.com/curious-arin/Customer-Lifetime-Value-Prediction-System/blob/main/images/14.correlation_heatmap_after_feature_engineering.png" width="100%">


### 15. Feature Distribution After Feature Engineering
- **Data is right skewed, so i will do log transformation after train test split**
<img src="https://github.com/curious-arin/Customer-Lifetime-Value-Prediction-System/blob/main/images/15.distribution_of_features_after_feature_engineering.png" width="100%">

-----

## ⚙️ Machine Learning Models
- Linear Regression
- K-Nearest Neighbors
- Decision Tree
- Random Forest
- XGBoost

-----


## 📈 Model Training & Evaluation

Five regression models were evaluated, followed by hyperparameter optimization using Optuna.

**Final model:** Tuned Random Forest Regressor

| Metric | Test result |
|---|---:|
| MAE | 638.34 |
| RMSE | 6997.01 |
| R² | 0.24 |

The final model achieved a test MAE of approximately **638.34 CLV units**, meaning its predictions differ from actual future customer spending by around 638 units on average in absolute terms.

The notebook scores indicates that the model is overfitting, so its generalization performance requires further improvement.

-----

## 🚀 Streamlit Application

- The trained Random Forest pipeline is saved using Joblib and integrated into a Streamlit application.
- Users can enter customer-level behavioral and purchasing information to generate a predicted CLV for the next 90 days.
- The application demonstrates how a machine learning model can turn historical customer data into an estimate that supports customer-value analysis.

-----

## 💼 Business Impact

This project demonstrates how e-commerce businesses can use historical purchase data to:

- Identify high-value customers.
- Understand customer purchasing behavior.
- Predict customer spending over the next 90 days.
- Support customer retention and targeted marketing.
- Improve customer segmentation and revenue planning.

-----

**⚠️ Note:** This project is still a work in progress, and Streamlit predictions should be treated as experimental due to current overfitting. Limited training data may be a contributing factor. I plan to revisit the project as more data becomes available.

## 🔮 Future Improvements

- Reduce overfitting and improve model generalization.
- Improve feature engineering as more customer data becomes available.
- Investigate large prediction errors and extreme CLV values.
- Implement MLOps practices for model tracking, monitoring, and retraining.
- Improve deployment with a more robust and scalable solution.
