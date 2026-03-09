import streamlit as st
import pandas as pd

st.title("HackSprint 2026: Day 1 Prep")

# Test Data for PDS Lab sync
data = pd.DataFrame({
    'Module': ['Python basics', 'Pandas', 'Streamlit'],
    'Status': ['Reviewing', 'Pending', 'Active']
})

st.table(data)
st.success("Environment Fixed. Commute ready.")