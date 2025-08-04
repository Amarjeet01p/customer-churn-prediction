import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("Telco-Customer-Churn.csv")
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df.dropna(inplace=True)
    df['TenureGroup'] = df['tenure'].apply(
        lambda t: '0–1 yr' if t <= 12 else '1–2 yrs' if t <= 24 else '2–4 yrs' if t <= 48 else '4+ yrs'
    )
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("🔎 Filter Data")
contract_type = st.sidebar.multiselect("Contract Type", df['Contract'].unique(), default=df['Contract'].unique())
payment_method = st.sidebar.multiselect("Payment Method", df['PaymentMethod'].unique(), default=df['PaymentMethod'].unique())

# Apply filters
filtered_df = df[
    (df['Contract'].isin(contract_type)) &
    (df['PaymentMethod'].isin(payment_method))
]

# Churn stats
churn_rate = filtered_df['Churn'].value_counts(normalize=True).get('Yes', 0)
st.markdown(f"## 📉 Churn Rate: **{churn_rate:.2%}**")
st.markdown(f"### Total Customers: `{filtered_df.shape[0]}`")

# Charts
col1, col2 = st.columns(2)

with col1:
    fig1 = px.histogram(filtered_df, x='InternetService', color='Churn', barmode='group', title='Churn by Internet Service')
    st.plotly_chart(fig1, use_container_width=True)

    fig3 = px.box(filtered_df, x='Churn', y='MonthlyCharges', color='Churn', title='Monthly Charges by Churn')
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    fig2 = px.histogram(filtered_df, x='TenureGroup', color='Churn', barmode='group', title='Churn by Tenure Group')
    st.plotly_chart(fig2, use_container_width=True)

    fig4 = px.pie(filtered_df, names='Churn', title='Churn Ratio')
    st.plotly_chart(fig4, use_container_width=True)
