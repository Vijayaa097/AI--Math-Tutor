import streamlit as st
import requests
import logging

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


st.title("AI Math Tutor")
math_problem = st.text_input("Enter a math problem:")

if st.button("Solve"):
    logger.info("Solve button clicked!")  
    response = requests.post("http://backend:8000/solve", json={"problem": math_problem})
    if response.status_code == 200:
        result = response.json()
        if "solution" in result:  # Check if 'solution' exists
            st.write("### Solution:", result["solution"])
            st.write("### Explanation:", result["explanation"])
        else:
            st.error(f"Error: {result.get('error', 'Unknown error')}")
    else:
        st.error("Error solving problem")
