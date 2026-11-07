def reply(text):
    if not text.strip():
        return "Please enter a message."

    return "Echo: " + text