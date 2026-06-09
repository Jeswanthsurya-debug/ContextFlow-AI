# ContextFlow-AI

## Chosen Vertical
Productivity & Task Management

## Approach and Logic
The solution utilizes a class-based architecture to maintain state (user history) and decouple the decision-making logic from the interface. It uses conditional branching based on `context` (Urgent vs. Creative) to ensure the assistant's tone and output are dynamically tailored to the user's immediate needs.

## How it works
1. Initialize the `DynamicAssistant` with a persona.
2. Pass an input and a context tag to the `get_response` method.
3. The system parses the context to determine the appropriate response strategy.

## Assumptions
- The assistant assumes input is sanitized text.
- The system is designed to be easily integrated into a larger API-driven backend.
