# File Variable
message_file="user_message.txt"

def save_message(message):
    try:
        # Context Manager using 'with'
        with open(message_file, "w") as f:
            f.write(message)
        print("Message created successfully")
    # Error Handling
    except Exception:
        print("Error: could not save the message")


def read_message(message_file):
    try:
        # Context Manager using 'with'
        with open(message_file, "r") as f:
            print(f.read())
    # Error handling
    except Exception:
        print("No saved message.")
