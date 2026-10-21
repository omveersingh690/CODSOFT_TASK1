
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import random

app = Flask(__name__)

def get_response(user_message):
    message = user_message.lower().strip()
    words = set(message.replace("?", "").replace("!", "").replace(".", "").split())

    if not message:
        return "Please enter a message."

    if words.intersection({"hello", "hi", "hey", "namaste"}):
        return random.choice([
            "Hello! Welcome to CodSoft Chatbot.",
            "Hi there! How can I help you?",
            "Hey! Nice to meet you."
        ])

    elif "your name" in message or "who are you" in message:
        return "I am CodSoft Chatbot, a rule-based conversational assistant."

    elif "how are you" in message:
        return "I am working perfectly! Thanks for asking. How can I help you?"

    elif "help" in words:
        return (
            "You can ask me about my name, Python, AI, "
            "the current time, today's date, or motivation."
        )

    elif "python" in words:
        return (
            "Python is a popular programming language used in "
            "AI, machine learning, automation, and web development."
        )

    elif "artificial intelligence" in message or "what is ai" in message:
        return (
            "Artificial Intelligence (AI) is the field of building "
            "systems that perform tasks requiring human-like intelligence."
        )

    elif "time" in words:
        return "Current time: " + datetime.now().strftime("%I:%M:%S %p")

    elif "date" in words or "today" in words:
        return "Today's date: " + datetime.now().strftime("%d %B %Y")

    elif "motivation" in words or "motivational" in words:
        return "Keep learning and improving every day. Small steps lead to big achievements!"

    elif words.intersection({"thanks", "thank", "thankyou"}):
        return "You're welcome! I am happy to help."

    elif words.intersection({"bye", "goodbye", "exit", "quit"}):
        return "Goodbye! Keep learning and have a wonderful day."

    else:
        return (
            "I don't have a rule for that question yet. "
            "Try asking about Python, AI, my name, time, date, or motivation."
        )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")

    if not isinstance(message, str):
        return jsonify({"reply": "Please send a valid text message."}), 400

    if len(message) > 1000:
        return jsonify({"reply": "Please keep your message under 1000 characters."}), 400

    return jsonify({"reply": get_response(message)})


if __name__ == "__main__":
    app.run(debug=True)
