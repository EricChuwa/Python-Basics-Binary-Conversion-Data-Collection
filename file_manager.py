#!/usr/bin/python3
message_file="user_message.txt"
def save_message(message):
    try:
        with open(message_file, "w") as f:
            f.write(message)
        print("Message created successfully")
    except Exception:
        print("Error: could not save the message")


def read_message(message_file):
    try:
        with open(message_file, "r") as f:
            print(f.read())
    except Exception:
        print("No saved message.")
