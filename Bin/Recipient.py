#Authored by mostly nick :)
import sys

# Prompt the user for input
character_name = input("Enter name of new character on Yggdrasil, if not same as on old server: ")

# Specify the file paths
argument_file = "References/Argument.txt"
recipient_file = "References/Recipient.txt"

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
