import os
import shutil

# Define the base directory and the target directories
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../queue'))
account_override_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../AccountOverride.txt'))
name_override_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../NameOverride.txt'))
raw_data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../RawData'))

# Delete existing files if they exist
if os.path.exists(account_override_file):
    os.remove(account_override_file)

if os.path.exists(name_override_file):
    os.remove(name_override_file)

# Ensure the RawData directory exists
os.makedirs(raw_data_dir, exist_ok=True)

# Check for directories in the base_dir
for account_name in os.listdir(base_dir):
    account_path = os.path.join(base_dir, account_name)

    if os.path.isdir(account_path):  # Ensure it is a directory
        for character_name in os.listdir(account_path):
            character_path = os.path.join(account_path, character_name)

            if os.path.isdir(character_path):  # Ensure it is a directory
                wtf_path = os.path.join(character_path, 'WTF')

                if os.path.isdir(wtf_path):  # Check if WTF folder exists
                    # Define the destination path for the WTF folder
                    destination_wtf_path = os.path.join(raw_data_dir, f"WTF")

                    # Delete the existing WTF folder in the destination if it exists
                    if os.path.exists(destination_wtf_path):
                        shutil.rmtree(destination_wtf_path)

                    # Save account name and character name to respective files
                    with open(account_override_file, 'a') as account_file:
                        account_file.write(f"{account_name}\n")

                    with open(name_override_file, 'a') as name_file:
                        name_file.write(f"{character_name}\n")

                    # Copy the WTF folder to the RawData directory
                    shutil.copytree(wtf_path, destination_wtf_path)
