from src.langgraphagenticai.state.state import State

class BasicChatBotNode:
    """
    Basic chat bot logic
    """
    def __init__(self, model):
        self.llm = model

    def process(self, state:State)->dict:
        """
        process state and generate a chatbot response
        """
        print("process")
        try:
            return {"messages": self.llm.invoke(state['messages'])}
        except Exception as e:
            print(f"error in basic chat bot node {e}")