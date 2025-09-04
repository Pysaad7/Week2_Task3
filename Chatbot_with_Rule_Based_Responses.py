import re

def chatbot():
    print("Chatbot is ready! Type 'exit' to quit.\n")

    # Patterns & Responses (Regex use karenge)
    patterns = {
        r"\b(hi|hello|hey)\b": "Hi, how can I help you?",
        r"\bwhat is your name\b": "I am your Python Chatbot.",
        r"\bhow are you\b": "I am just a bot, but I am doing fine!",
        r"\bbye\b": "Goodbye! Have a nice day.",
        r"\bhelp\b": "You can ask me about my name, greetings, or how I am.",
        r"\bthank(s| you)\b": "You're welcome!"
    }

    while True:
        # User input
        user_input = input("You: ").lower()

        # Exit condition
        if user_input == "exit":
            print("Bot: Exiting... Goodbye!")
            break

        matched = False
        # Regex matching
        for pattern, response in patterns.items():
            if re.search(pattern, user_input):
                print("Bot:", response)
                matched = True
                break

        if not matched:
            print("Bot: I don't understand.")

# Run chatbot
chatbot()
