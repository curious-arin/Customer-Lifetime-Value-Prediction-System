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

---

## 📈 Dataset 

[Original Online Retail Dataset — Kaggle](https://www.kaggle.com/datasets/vijayuv/onlineretail)

- **Original Dataset Columns:** ['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country']
- **Original Dataset Overview:** The data has 541909 rows, 8 columns and it does not have important features like recency, frequency, monetary and clv.

[Prepared Dataset](https://www.kaggle.com/datasets/neuralarin/customer-lifetime-value-dataset)

- **Prepared Dataset Columns:** ['Recency', 'Frequency', 'Monetary', 'CLV', 'TotalQuantity', 'UniqueProducts', 'ActiveDays', 'CustomerTenureDays', 'AverageUnitPrice', 'AverageQuantity', 'AverageTransactionValue', 'UniqueCountries']
- **Prepared Dataset Overview:** The data has 3370 rows and 12 columns

---

## 🔍 Some Interesting Prepared Feature Overview 

- **Recency:** How many days since the customer’s last purchase
- **Frequency:** How many different orders the customer made
- **Monetary:** Total money spent by the customer
- **CLV:** Total amount the customer spends during the 90-day period.

---

## 🚀 How to Run the Application Locally

Follow these steps to run the application on your local system.

### 1. Clone the Repository

```bash
git clone https://github.com/neuralarin/Customer-Lifetime-Value-Prediction-System.git

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

---

## 🔄 Complete Project Workflow

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

---

## 📊 Exploratory Data Analysis & Key Findings

### 1. What is the distribution of cancelled invoices?

![Cancelled invoices](images/cancelled_invoices.png)

**Insight:** The dataset contains 9,288 cancelled invoices.

### 2. How has revenue changed over time?

![Total revenue over time](images/total_revenue_over_time.png)

**Insight:** Revenue remains relatively stable before showing a substantial spike.

### 3. Which countries generate the most revenue?

![Top revenue generating countries](images/top_10_revenue_countries.png)

**Insight:** The United Kingdom generates the highest revenue.

### 4. Which products generate the highest revenue?

![Top revenue generating products](images/top_products_by_revenue.png)

**Insight:** PAPER CRAFT, LITTLE BIRDIE is the highest-revenue product in the analysis.

### 5. Which products sell the most by quantity?

![Top products by quantity sold](images/top_products_by_quantity_sold.png)

**Insight:** PAPER CRAFT, LITTLE BIRDIE and MEDIUM CERAMIC TOP STORAGE JAR are among the top-selling products.

### 6. Which month generates the most revenue?

![Monthly revenue](images/monthly_revenue.png)

**Insight:** Monthly revenue increases overall and peaks in November.

### 7. Which weekdays perform best?

![Revenue share by weekday](images/revenue_share_by_weekday.png)

**Insight:** Tuesday and Thursday generate the largest shares of revenue.

### 8. How many products are typically purchased per order?

![Items per order](images/items_per_order.png)

**Insight:** Order quantities are generally low, with some extreme outliers.

### 9. Who are the highest-revenue customers?

![Customers by revenue](images/customers_by_revenue.png)

**Insight:** Customer ID `14646` generates the highest revenue in the analysis.

### 10. How many customers are repeat versus one-time buyers?

![Repeat versus one-time customers](images/repeat_vs_onetime_customers.png)

**Insight:** Approximately 65.6% of customers are repeat buyers, while 34.4% are one-time buyers.

### 11. How are numerical features correlated?

![Correlation heatmap](images/correlation_heatmap.png)

**Insight:** Quantity and TotalPrice have a strong positive correlation of approximately 0.91.

### 12. How is Customer Lifetime Value distributed?

![CLV distribution](images/clv_distribution.png)

**Insight:** CLV is highly right-skewed. Most customers generate relatively low future revenue, while a smaller group contributes much higher value.

### 13. Which features are most strongly associated with CLV?

![CLV correlation heatmap](images/correlation_heatmap2.png)

**Insight:** TotalQuantity has the strongest reported positive correlation with CLV at approximately 0.76, followed by Monetary at approximately 0.65.

---

## 🧹 Data Preprocessing

- Removed transactions with missing customer identifiers.
- Identified cancelled invoices and excluded the cancellation indicator from the modeling dataset.
- Handled missing product descriptions.
- Created the `TotalPrice` feature.
- Constructed customer-level RFM and additional behavioral features.
- Created the future 90-day CLV target using a time-based split.
- Applied feature transformations and target log transformation.

---

## 📈 Model Training & Evaluation

Five regression models were evaluated, followed by hyperparameter optimization using Optuna.

**Final model:** Tuned Random Forest Regressor

| Metric | Test result |
|---|---:|
| MAE | 638.34 |
| RMSE | See notebook output |
| R² | See notebook output |

The final model achieved a test MAE of approximately **638.34 CLV units**, meaning its predictions differ from actual future customer spending by around 638 units on average in absolute terms.

The notebook also indicates that the model is overfitting, so its generalization performance requires further improvement.

---

## 🛠️ Tech Stack

- **Programming:** Python
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn, XGBoost
- **Hyperparameter Optimization:** Optuna
- **Model Persistence:** Joblib
- **Application Deployment:** Streamlit
- **Development Environment:** Jupyter Notebook

---

## 🚀 Streamlit Application

The trained Random Forest pipeline is saved using Joblib and integrated into a Streamlit application.

Users can enter customer-level behavioral and purchasing information to generate a predicted CLV for the next 90 days.

The application demonstrates how a machine learning model can turn historical customer data into an estimate that supports customer-value analysis.

---

## 💼 Business Impact

This project demonstrates how e-commerce businesses can use historical purchasing patterns to:

- Identify high-value customers.
- Understand repeat purchasing behavior.
- Estimate future customer revenue.
- Support customer retention and marketing strategies.
- Inform customer segmentation and revenue planning.

These are potential business applications; their actual impact would need to be validated in a production setting.

---

## 🔮 Future Improvements

- Reduce overfitting and improve generalization.
- Improve feature engineering and customer behavior indicators.
- Evaluate performance across customer segments.
- Analyze large prediction errors and extreme CLV values.
- Use time-based validation to better reflect future predictions.
- Add model explainability to understand the drivers of predicted CLV.
- Monitor model performance as new transactions become available.
- Improve the Streamlit interface with prediction explanations and customer-value categories.
