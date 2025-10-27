# Validating user input
def validate_input(user_input):
    if user_input == "":
        return False
    else:
        return True

    
def convert_to_binary(text):
    
    # Variable 
    binary = ""

    if type(text) == str:
        for char in text:
            bin_val = bin(ord(char))[2: ]
            binary += f"{bin_val} "

    elif type(text) == int:
        binary = bin(text)

    return binary

def create_message(name, age, name_binary, age_binary):
    message = f"Hello {name}, you are {age} years old!\nName in binary: {name_binary}\nAge in binary: {age_binary}"
    return message
