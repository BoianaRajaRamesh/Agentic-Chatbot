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
        return {"message": self.llm.invoke(state['message'])}