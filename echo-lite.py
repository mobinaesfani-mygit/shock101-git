def reply(text):
    if not text.strip():
        return "Please enter a message."

    return "Echo: " + text

user_input = input("You: ")
print("OK")
print(reply(user_input))