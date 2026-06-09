"""
ContextFlow-AI: A modular, context-aware decision assistant.
Focus: Clean code, logical decision-making, and maintainability.
"""

class DynamicAssistant:
    def __init__(self, persona="General Assistant"):
        self.persona = persona
        self.history = []

    def get_response(self, user_input, context):
        """Logical decision-making engine."""
        self.history.append({"input": user_input, "context": context})
        
        # Logic based on context and persona
        if context.lower() == "urgent":
            return f"[{self.persona}] ALERT: Prioritizing '{user_input}'. Handling immediately."
        elif context.lower() == "creative":
            return f"[{self.persona}] Let's brainstorm on '{user_input}'—what if we approach this from a new angle?"
        else:
            return f"[{self.persona}] Received: '{user_input}'. Processing with standard parameters."

def main():
    # Demonstrating the assistant
    ai = DynamicAssistant(persona="Project Manager")
    
    # Simulate a dynamic interaction
    print(ai.get_response("Finish report", "urgent"))
    print(ai.get_response("Logo design ideas", "creative"))

if __name__ == "__main__":
    main()
