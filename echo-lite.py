def reply(text):
    if not text.strip():
        return "Please enter a message."

    if text.strip().lower() in ["hi", "hello"]:
        return "Hello! How can I help you?"

    return "Echo: " + text



assert reply("Hello") == "Hello! How can I help you?"
assert reply("   ") == "Please enter a message."
assert reply("hello") == "Hello! How can I help you?"
print("Test passed!")


if __name__ == "__main__":
    user_input = input("You: ")
    print("OK")
    print(reply(user_input))