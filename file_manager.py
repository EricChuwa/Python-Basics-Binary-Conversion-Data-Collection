#!/usr/bin/python3

def save_message(message):
    try:
        with open("user_message.txt", "w") as f:
            f.write(message)
        print("Message created successfully")
    except Exception:
        print("Error: could not save the message")


def read_message():
    try:
        with open("user_message.txt", "r") as f:
            print(f.read())
    except Exception:
        print("No saved message.")
