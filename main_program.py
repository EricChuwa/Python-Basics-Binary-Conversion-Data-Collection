#!/usr/bin/python3
from helper_functions import validate_input, convert_to_binary, create_message
from file_manager import save_message, read_message
from greetings import show_intro, show_exit_message

def get_user_info():
    Valid = False
    while True: # This Whil Loop is for name 
        user_name = input("Enter Name: ")

        if not validate_input(user_name):
            print("Invalid name! Please try again.")
            continue
        
        while not Valid:  # This second While loop is for age  
            user_age = input("Enter Age: ")
            
            if not user_age.isdigit():
                print("Invalid age! Please enter a number.")
                continue
            
            return user_name, user_age


if __name__ == "__main__":
     show_intro()
     inputs=get_user_info()
     name_bin=convert_to_binary(inputs[0])
     age_bin=convert_to_binary(inputs[1])
     message=create_message(inputs[0], inputs[1], name_bin, age_bin)
     message_file="user_message.txt"
     save_message(message)
     read_message(message_file)
     show_exit_message()
