# 📉 Customer Churn Prediction

Predict which telecom customers are likely to leave and suggest actionable retention strategies using machine learning and data analysis.

## 🧠 Project Overview

This project analyzes customer behavior and predicts churn using:
- SQL for data exploration
- Python for preprocessing & modeling
- Plotly + ipywidgets for an interactive dashboard

## 📂 Files

| File                         | Description                          |
|------------------------------|--------------------------------------|
| `Customer_Churn_Prediction.ipynb` | Main Colab notebook with EDA, modeling, and results |
| `Telco-Customer-Churn.csv`  | Original dataset                     |
| `churn_report.html`         | Optional static report with visuals  |
| `app.py`                    | (Optional) Streamlit dashboard code  |
| `requirements.txt`          | Python dependencies                  |

## 📊 Tools & Technologies
- Python (pandas, scikit-learn, plotly, ipywidgets)
- SQLite + SQL queries
- Google Colab
- Streamlit (optional)

## 🔍 Key Insights
- Month-to-month contracts had the highest churn (43%)
- Electronic check users churn more than auto-payment users
- Long-tenure customers are much less likely to churn

## ⚙️ How to Run

1. Clone the repo
2. Open `Customer_Churn_Prediction.ipynb` in Colab or Jupyter
3. Run all cells to explore data and model predictions
4. (Optional) Run `app.py` locally with Streamlit:

```bash
streamlit run app.py
