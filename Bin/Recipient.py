import sys
import os

# Specify the file paths
argument_file = "References/Argument.txt"
recipient_file = "References/Recipient.txt"
name_override_file = "../NameOverride.txt"

# Check if NameOverride.txt exists
if os.path.exists(name_override_file):
    # If it exists, write its contents to Recipient.txt
    try:
        with open(name_override_file, 'r') as src, open(recipient_file, 'w') as dest:
            dest.write(src.read())
        print(f"Character name from '{name_override_file}' has been saved as recipient.")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    # Prompt the user for input
    character_name = input("Enter name of new character on Yggdrasil, if not same as on old server: ")

    if character_name:
        # User provided input, write it to Recipient.txt
        with open(recipient_file, 'w') as file:
            file.write(character_name)
        print(f"Character name '{character_name}' has been saved as recipient.")
    else:
        # No input provided, copy contents of Argument.txt to Recipient.txt
        try:
            with open(argument_file, 'r') as src, open(recipient_file, 'w') as dest:
                dest.write(src.read())
            print(f"Continuing with same name as on old server.")
        except FileNotFoundError:
            print(f"CRITICAL ERROR: Cached character file(s) not found, terminating!")
            selection = input("")
            parent_pid = os.getppid()  # Get the parent process ID
            os.kill(parent_pid, 9)  # Send SIGKILL signal to the parent
