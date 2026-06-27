import random

def chatbot():
    print("Chatbot: Hello! I am your assistant. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if user_input == "bye":
            print("Chatbot: Goodbye! Have a great day.")
            break

        # Greeting responses
        elif user_input in ["hi", "hello", "hey"]:
            responses = [
                "Hello! How can I help you today?",
                "Hi there! What can I do for you?",
                "Hey! Feel free to ask me something."
            ]
            print("Chatbot:", random.choice(responses))

        # Asking about chatbot
        elif "your name" in user_input:
            print("Chatbot: I am a simple rule-based chatbot created using Python.")

        # Asking about help
        elif "help" in user_input:
            print("Chatbot: I can answer simple questions like greetings, time, and general queries.")

        # Asking about time
        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print("Chatbot: The current time is", current_time)

        # Asking about internship
        elif "internship" in user_input:
            print("Chatbot: Internships help students gain practical experience in real-world environments.")

        # Default response
        else:
            fallback = [
                "I'm not sure I understand. Could you rephrase?",
                "Interesting question! Can you explain a bit more?",
                "Sorry, I don't have an answer for that yet."
            ]
            print("Chatbot:", random.choice(fallback))


# Run chatbot
chatbot()
