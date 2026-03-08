import streamlit as st
import pandas as pd
import numpy as np

# This is the 'CSS Injection' we discussed for your teammate
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    stButton>button {
        color: #4F8BF9;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("HackSprint 2026: Team Strategy")
st.write("Target: Top 10 Finalists for Day 3 [cite: 53, 58]")

# Creating a dummy dataset to test Pandas
data = pd.DataFrame({
    'Task': ['Install Tools', 'Learn Pandas', 'Hackathon Day 1'],
    'Status': ['Completed', 'In Progress', 'Pending']
})

st.table(data)

if st.button('Click for Ayanokoji’s Insight'):
    st.success("Preparation is the only way to minimize variables. You are now ahead.")