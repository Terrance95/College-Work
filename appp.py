import streamlit as st
import google.generativeai as genai
import os

# 1. FORGET THE .env FILE FOR NOW
# Paste your actual key between the quotes below
MY_API_KEY = "AIzaSyDj-uCCK089Z91TbrxPh1LKuYL88P6xV00" 

# 2. CONFIGURE THE BRAIN DIRECTLY
genai.configure(api_key=MY_API_KEY)

# Force the library to use the stable 'v1' API
genai.configure(api_key=MY_API_KEY, transport='rest') 

def get_ai_response(system_prompt, user_input):
    # Simulated AI Response for the Demo
    return """
    ### 🚀 Engineering Student To-Do List:
    1. **EDL (Electrical Design Lab):** Complete the circuit schematic for the frequency generator.
    2. **Civil Assignment:** Finalize the structural analysis report for the bridge model.
    3. **Math Prep:** Review Triple Integrals for the Monday morning quiz.
    4. **Hackathon:** Finalize the UI styling and API documentation.
    """
    
# 3. THE UI (The Skeleton)
st.set_page_config(page_title="Hacksprint MVP", layout="wide")

st.title("🚀 Team [Your Name] Solution")

with st.sidebar:
    st.header("Inputs")
    # Add generic inputs tonight (Text area, Sliders)
    user_input = st.text_area("Enter Problem Details:")

if st.button("Generate Solution"):
    with st.spinner("AI is architecting..."):
        # This part will be filled on Monday once you know the problem
        result = get_ai_response("You are an expert solver...", user_input)
        st.write(result)