import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="REVA CSIT - Data Engine", layout="wide")

st.title("🚀 CSIT Semester 2: Data Mastery")
st.subheader("HackSprint & PDS Lab Integration")

# 1. Sidebar for Inputs
st.sidebar.header("Control Panel")
uploaded_file = st.sidebar.file_saver = st.sidebar.file_uploader("Upload PDS Lab CSV", type="csv")

# 2. Main Dashboard Logic
col1, col2 = st.columns(2)

with col1:
    st.info("Subject Strategy")
    st.write("- **PDS:** Focus on Vectorization (NumPy)")
    st.write("- **ACP:** Focus on Memory Management in C")

with col2:
    st.success("10 SGPA Progress")
    progress = st.slider("Semester Completion", 0, 100, 15)
    st.progress(progress)

# 3. Data Simulation (Hackathon Practice)
st.divider()
st.write("### Live Data Preview")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Algorithm A', 'Algorithm B', 'Algorithm C'])
st.line_chart(chart_data)