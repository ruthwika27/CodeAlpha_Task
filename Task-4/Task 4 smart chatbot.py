
# ------------------------------------------
# CodeAlpha Task 4: Smart ChatBot
# Created by: Ruthwika
# Description: A smart rule-based chatbot covering greetings, time/date, jokes, math help, and more.
# ------------------------------------------

import time
from datetime import datetime

def show_time():
    return datetime.now().strftime("%I:%M %p")

def show_date():
    return datetime.now().strftime("%A, %d %B %Y")

def tell_joke():
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything! 😂",
        "Why did the computer go to the doctor? Because it had a virus! 🦠",
        "Why did the math book look sad? Because it had too many problems. 😅"
    ]
    return jokes[int(time.time()) % len(jokes)]  # Rotate joke based on time

def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello there! 😊 How can I assist you today?"

    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking. What can I do for you?"

    elif "name" in user_input:
        return "I'm SmartChatBot, created by Ruthwika as part of CodeAlpha! 🤖"

    elif "creator" in user_input or "who made you" in user_input:
        return "I was proudly created by Ruthwika for a CodeAlpha task. 🚀"

    elif "time" in user_input:
        return f"The current time is {show_time()}"

    elif "date" in user_input:
        return f"Today's date is {show_date()}"

    elif "help" in user_input:
        return ("I can respond to greetings, tell jokes, show time/date, do basic math, "
                "talk about my creator, and more!")

    elif "weather" in user_input:
        return "I'm not connected to live weather, but I hope it's bright and sunny! ☀️"

    elif "thank" in user_input:
        return "You're welcome! 😊"

    elif "joke" in user_input:
        return tell_joke()

    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! 👋 Take care and have a great day!"

    elif "color" in user_input:
        return "I like blue – it's the color of logic and calm! 💙"

    elif "food" in user_input:
        return "I'm a bot – I feed on code, not food 😄"

    elif "math" in user_input:
        return "Sure! Try asking me a basic math expression like 5 + 3"

    # Evaluate math expression
    try:
        if any(op in user_input for op in ['+', '-', '*', '/']):
            result = eval(user_input)
            return f"The answer is {result}"
    except:
        return "That doesn't seem like a valid math expression."

    # Default
    return "Hmm, I didn't quite understand that. Try asking for 'help'."

def run_chatbot():
    print("="*55)
    print("🤖 Welcome to SmartChatBot - CodeAlpha Task 4 by Ruthwika")
    print("💡 Type 'exit' to end the chat at any time.")
    print("="*55)
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("SmartChatBot: Chat ended. Thanks for using me! 🌟")
            break

        response = get_response(user_input)
        print(f"SmartChatBot: {response}")
        time.sleep(1)

# Run the chatbot
run_chatbot()
