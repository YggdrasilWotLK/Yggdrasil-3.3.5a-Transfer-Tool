import os

file_path = 'TERMINATERETAIL.txt'

# Check if the file exists
if os.path.exists(file_path):
    parent_pid = os.getppid()  # Get the parent process ID
    os.kill(parent_pid, 9)  # Send SIGKILL signal to the parent
else:
    print(f"Welcome to Yggdrasil's WotLK 3.3.5a toon transfer utility!")