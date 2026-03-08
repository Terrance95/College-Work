import streamlit as st
import pandas as pd
import numpy as np

# FIX: Ensure the triple quotes open and close properly
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("HackSprint 2026: Team Strategy")
st.write("Target: Top 10 Finalists [cite: 53]")

# Test Data
data = pd.DataFrame({
    'Task': ['Install Tools', 'Learn Pandas', 'Hackathon Day 1'],
    'Status': ['Completed', 'In Progress', 'Pending']
})

st.table(data)