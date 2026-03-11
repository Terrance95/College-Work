import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="WealthEngine 2026", layout="wide")

st.title("💰 Smart Wealth Predictor")
st.markdown("---")

# 1. Input Section
st.sidebar.header("User Financial Data")
income = st.sidebar.number_input("Monthly Income (₹)", min_value=0, value=50000)
expenses = st.sidebar.number_input("Monthly Expenses (₹)", min_value=0, value=20000)
interest = st.sidebar.slider("Annual Interest Rate (%)", 1, 20, 8)

monthly_savings = income - expenses

# 2. Logic: The Wealth Projection Engine
years = 5
months = years * 12
data = []
current_wealth = 0

for m in range(1, months + 1):
    # Compound interest calculation (Monthly)
    current_wealth = (current_wealth + monthly_savings) * (1 + (interest/100)/12)
    data.append(current_wealth)

# 3. Display Results
col1, col2 = st.columns(2)

with col1:
    st.metric("Monthly Savings", f"₹{monthly_savings}")
    st.metric(f"Wealth after {years} Years", f"₹{int(current_wealth)}")

with col2:
    # Create a DataFrame for visualization
    df = pd.DataFrame(data, columns=["Projected Wealth"])
    st.line_chart(df)

# 4. The Data Science Table
st.write("### Raw Monthly Projection")
st.dataframe(df.tail(12)) # Shows the last year