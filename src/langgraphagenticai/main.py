import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUi
from src.langgraphagenticai.LLMs.GroqLlm import GroqLlm
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    """
    loads and run the langgraph agentic ai application with help of streamlit ui
    """
    ui = LoadStreamlitUi()
    user_input = ui.load_ui()

    if not user_input:
        st.error("Error: Fail to load user input")
        return

    user_message = st.chat_input("Enter your message")
    if user_message:
        try:
            obj_llm = GroqLlm(user_input = user_input)
            print(obj_llm)
            model = obj_llm.get_llm_model()
            print("model", model)

            if not model:
                st.error("Error: LLm model not initilized")
                return
            
            usecase = user_input.get("selected_use_case")
            if not usecase:
                st.error("Error: No usecase selected")
                return
            print("usecase", usecase)
            graph_bilder = GraphBuilder(model=model)
            try:
                graph = graph_bilder.setup_graph(usecase=usecase)
                print("graph", graph)
                d = DisplayResultStreamlit(usecase=usecase, graph=graph, user_message=user_message)
                d.display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph setup failed {e}")
                return
            


        except Exception as e:
            print(f"Error {e}")
            st.error(f"Error: {e}")
            return