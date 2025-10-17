import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLlm:
    def __init__(self, user_input):
        self.user_input = user_input

    def get_llm_model(self):
        try:
            groq_api_key = self.user_input['GROQ_API_KEY']
            selected_model = self.user_input['selected_model']
            if groq_api_key == "" or not groq_api_key or os.environ["GROQ_API_KEY"]:
                st.error("Please enter api key")

            llm = ChatGroq(api_key=groq_api_key, model=selected_model)
        except Exception as e:
            raise ValueError(f"Error occured with exception {e}")
        
        return llm