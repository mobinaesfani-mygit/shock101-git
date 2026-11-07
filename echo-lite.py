def reply(text):
    if not text.strip():
        return "Please enter a message."

    return "Echo: " + text



assert reply("Hello") == "Echo: Hello"
print("Test passed!")


if __name__ == "__main__":
    user_input = input("You: ")
    print("OK")
    print(reply(user_input))