def chatbot():
    print("Chatbot is ready! When you Type Exit its Quit.\n")

    # Pattrens & Responses
    pattrens = {
        "hello": "Hi, how can I help you?",
        "hi": "Hi, how can I help you?",
        "hey": "Hello! How are you?",
        "what is your name": "I am your Python Chatbot.",
        "how are you": "I am just a bot, but I am doing fine!",
        "bye": "Goodbye! Have a nice day.",
        "help": "You can ask me about my name, greetings, or how I am.",
        "thank you": "You're welcome!"      
    }

    while True:
        # User input
        user_input = input("You: ").lower()

        # Exit condition
        if user_input == "exit":
            print("Bot: Exiting... Goodbye!")
            break

        matched = False
        # Keyword matching
        for pattren, response in pattrens.items():
            if pattren in user_input:
                print("Bot:", response)
                matched = True
                break

        if not matched:
            print("Bot: I don't understand.")

# Run the chatbot
chatbot()