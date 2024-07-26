import streamlit as st # for UI
import os
from dotenv import load_dotenv # to load environment variables
load_dotenv() # load all the env variables

import google.generativeai as genai

# Configuring the Google Generative AI API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

# Function to generate response from the LLM
def get_gemini_response(ques):
    resp = model.generate_content(ques)
    return resp.text

# Setting up the Streamlit app
st.set_page_config(
    page_title="Gemini Pro Q/A Project",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Setting up the header
st.header("Gemini Q/A App")

# Input field for the question
question = st.text_input("Ask a question:")

# Submit button to get the response
if st.button("Submit"):
    response = get_gemini_response(question)
    st.write("User:", question)
    st.write("Bot:", response)
