
import random
from datetime import datetime

def chatbot_response(user_input):
    message = user_input.lower().strip()

    if any(word in message for word in ["hello", "hi", "hey"]):
        return random.choice([
            "Hello! How can I help you?",
            "Hi there! Nice to meet you.",
            "Hey! What would you like to know?"
        ])

    elif "your name" in message or "who are you" in message:
        return "I am CodSoftBot, a simple rule-based chatbot."

    elif "how are you" in message:
        return "I am doing great! Thanks for asking."

    elif "time" in message:
        return "The current time is " + datetime.now().strftime("%I:%M %p")

    elif "date" in message or "today" in message:
        return "Today's date is " + datetime.now().strftime("%d-%m-%Y")

    elif "help" in message:
        return "You can ask me about my name, time, date, or simply say hello."

    elif "thank" in message:
        return "You're welcome! Happy to help."

    elif any(word in message for word in ["bye", "goodbye", "exit", "quit"]):
        return "Goodbye! Have a wonderful day."

    else:
        return "Sorry, I don't understand that yet. Try asking for help."


def main():
    print("=" * 45)
    print("       WELCOME TO CODSOFT CHATBOT")
    print("=" * 45)
    print("Type 'help' to see what I can do.")
    print("Type 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("Bot: Please enter a message.\n")
            continue

        response = chatbot_response(user_input)
        print("Bot:", response, "\n")

        if any(word in user_input.lower().split()
               for word in ["bye", "goodbye", "exit", "quit"]):
            break


if __name__ == "__main__":
    main()
