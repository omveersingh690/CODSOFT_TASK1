
# CodSoft Task 1: Rule-Based Chatbot

A Python-based rule-driven chatbot developed for Task 1 of the CodSoft Artificial Intelligence Internship.

## Features
- Interactive web-based chat interface
- Rule-based responses using Python conditions
- Keyword matching and predefined responses
- Greetings, help, Python and AI explanations
- Current date and time responses
- Motivation and goodbye messages
- Input validation and unknown-question handling

## Technologies
- Python
- Flask
- HTML
- CSS
- JavaScript

## Project Structure
```text
CODSOFT_TASK1/
├── app.py
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

## Installation and Setup

1. Install Python 3.
2. Open a terminal in the project folder.
3. Create and activate a virtual environment:

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

4. Install dependencies:
```bash
python -m pip install -r requirements.txt
```

5. Start the application:
```bash
python app.py
```

6. Open http://127.0.0.1:5000 in your browser.

## How It Works
The Flask server receives a message from the browser and passes it to a Python function. The function normalizes the text, checks predefined conditions, and returns a matching response as JSON. JavaScript displays that response in the chat window.

## Learning Outcomes
- Python functions and conditional statements
- Basic natural language input processing
- Flask routes and JSON APIs
- Connecting frontend and backend code

## Internship
CodSoft Artificial Intelligence Internship — Task 1

Note: This is a rule-based chatbot, not a generative AI or machine learning model.
