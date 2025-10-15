import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfig import Config

class LoadStreamlitUi:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(), layout="wide")
        st.header("🤖 "+self.config.get_page_title())

        with st.sidebar:
            llm_options = self.config.get_llm_options()
            
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                model_options = self.config.get_groq_model_options()
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"]= st.text_input("Enter API Key", type="password")
                self.user_controls["selected_model"] = st.selectbox("Select Model", model_options)

            use_case_options = self.config.get_usecase_options()
            
            self.user_controls["selected_use_case"] = st.selectbox("Select Usecase", use_case_options)

        
        return self.user_controls