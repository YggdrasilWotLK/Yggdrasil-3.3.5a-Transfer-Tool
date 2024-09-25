# Authored by mostly Nick :)
import os
import shutil

def clean_raw_data():
    """Cleans the ../RawData folder, preserving only the 'Account' folder and '.gitignore' files."""

    raw_data_path = "../RawData"

    # Check if RawData folder exists
    if not os.path.exists(raw_data_path):
        # print(f"Error: RawData folder '{raw_data_path}' does not exist.")
        return

    # Check if Account folder exists within RawData
    account_path = os.path.join(raw_data_path, "Account")
    if not os.path.exists(account_path):
        return

    # Get a list of all files and folders in RawData except Account and .gitignore
    items_to_delete = [item for item in os.listdir(raw_data_path) if item not in ("Account", ".gitignore")]

    # Delete each item in the list
    for item in items_to_delete:
        item_path = os.path.join(raw_data_path, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)

if __name__ == "__main__":
    clean_raw_data()
