# 🛍️ Customer Segmentation and Marketing Analytics

This project aims to identify distinct customer segments using clustering techniques on a large retail transaction dataset. The insights are used to develop tailored marketing strategies and optimize business performance.

---

## 📁 Dataset

**Source**: [Kaggle - Retail Analysis Large Dataset](https://www.kaggle.com/datasets/sahilprajapati143/retail-analysis-large-dataset)  
**Size**: Over 250,000+ rows  
**Features Include**:
- Customer demographics (Name, Age, Gender, Country, Income)
- Transaction data (Product Category, Amount, Purchase Date, Quantity)
- Behavioral fields (Payment method, Order status, Ratings)

---

## 🎯 Objective

To segment customers based on behavioral and demographic factors and extract actionable business insights that can inform personalized marketing strategies and revenue optimization.

---

## 🧠 Methodology

### 1. Data Cleaning & Preparation
- Removed inconsistent and duplicate records
- Standardized demographic features
- Derived new fields: Frequency, Monetary, Recency
- Created a unique customer identifier (`New_Customer_ID`) using email

### 2. Feature Engineering
- Aggregated transactional records at the customer level
- Encoded categorical variables for clustering
- Imputed consistent demographic values based on cluster-specific logic

### 3. Clustering Scenarios
- **Scenario 1**: `Age + Frequency + Spend`
- **Scenario 2**: `Frequency + Spend`

### 4. Clustering Algorithms
- Applied **KMeans** clustering
- Determined optimal clusters using the **Elbow Method**
- Reduced dimensionality with **PCA** for visualization

### 5. Visualization
- Built Power BI dashboards:
  - **Page 1**: Customer demographics and data overview
  - **Page 2**: Cluster profiles, segment size, spend, and purchase patterns

---

## 💻 Tech Stack

| Category        | Tools / Libraries                                |
|----------------|---------------------------------------------------|
| Language        | Python 3.9                                        |
| Data Handling   | `pandas`, `numpy`                                 |
| ML/Clustering   | `scikit-learn` (KMeans, PCA), `elbow-method`     |
| Visualization   | `matplotlib`, `seaborn`, `plotly`                |
| Dashboarding    | Microsoft Power BI                                |
| Deployment (optional) | AWS SageMaker, Flask API, Docker, Lambda         |
| IDEs & Tools    | Jupyter Notebook, VSCode, Power BI Desktop        |

---

## 📊 Key Insights

- **Cluster 3** is the wealthiest and most active, contributing over **$263M** in sales.
- **Cluster 2** represents younger, low-income customers with minimal spend.
- Gender and income skew differently across clusters, providing targeting opportunities.

---

## 🚀 Deployment Plan (Optional)

A deployment-ready ML model (KMeans) can be exported and served via:
- **AWS SageMaker** for scalable real-time inference
- **Flask API** on **EC2**
- **Docker + Lambda + API Gateway** (lightweight serverless option)

---

## 📁 Files and Structure

```bash
├── notebooks/
│   └── customer_segmentation.ipynb     # Main modeling and analysis notebook
├── data/
│   └── raw/                            # Original Kaggle dataset
│   └── processed/                      # Cleaned and aggregated data
├── visuals/
│   └── cluster_visuals/                # PNGs of PCA plots and Elbow curves
├── deployment/
│   └── inference.py                    # Entry point for AWS deployment
├── dashboards/
│   └── powerbi_cluster_overview.pbix   # Power BI dashboards
└── README.md                           # Project overview
