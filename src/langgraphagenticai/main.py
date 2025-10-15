import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUi

def load_langgraph_agenticai_app():
    """
    loads and run the langgraph agentic ai application with help of streamlit ui
    """
    ui = LoadStreamlitUi()
    user_input = ui.load_ui()

    if not user_input:
        st.error("Error: Fail to load user input")

    user_message = st.chat_input("Enter your message")