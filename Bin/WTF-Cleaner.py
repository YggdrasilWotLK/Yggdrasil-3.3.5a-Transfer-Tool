import os
import shutil

print(f"Running WTF-Cleaner.py!")

def move_wtf_contents(base_dir):
    wtf_dir = os.path.join(base_dir, 'WTF')
    
    if os.path.exists(wtf_dir) and os.path.isdir(wtf_dir):
        items = os.listdir(wtf_dir)
        
        for item in items:
            source_path = os.path.join(wtf_dir, item)
            destination_path = os.path.join(base_dir, item)
            
            # Check if the destination already exists
            if os.path.exists(destination_path):
                # Remove the existing directory or file
                if os.path.isdir(destination_path):
                    shutil.rmtree(destination_path)
                    print(f"Removed existing directory: {destination_path}")
                else:
                    os.remove(destination_path)
                    print(f"Removed existing file: {destination_path}")

            shutil.move(source_path, destination_path)
        
        # Remove the WTF directory if it is empty after moving
        if not os.listdir(wtf_dir):
            os.rmdir(wtf_dir)
            
def list_folders_in_account(base_dir):
    account_dir = os.path.join(base_dir, 'Account')
    
    if os.path.exists(account_dir) and os.path.isdir(account_dir):
        items = os.listdir(account_dir)
        # Check for folders with an uppercase "A"
        folders = [item for item in items if os.path.isdir(os.path.join(account_dir, item))]
        
        if folders:
            print("Account-based structure identified. Available accounts:")
            for idx, folder in enumerate(folders):
                print(f"{idx + 1}. {folder}")
            return folders
        else:
            print("ERROR: No accounts found!")
            return []
    else:
        print(f"ERROR: Account directory does not exist at: {account_dir}")
        return []

def move_contents(selected_folder, base_dir):
    source_dir = os.path.join(base_dir, 'Account', selected_folder)
    
    if os.path.exists(source_dir) and os.path.isdir(source_dir):
        items = os.listdir(source_dir)
        
        for item in items:
            source_path = os.path.join(source_dir, item)
            destination_path = os.path.join(base_dir, item)
            
            # Avoid moving the account folder itself
            if os.path.isdir(source_path) and source_path == os.path.join(base_dir, 'Account'):
                continue
            
            if os.path.exists(destination_path):
                print(f"WARNING: Conflict with existing item at {destination_path}. Skipping '{source_path}'. You may have old files in the transfer Bin/Raw directory you need to delete.")
            else:
                shutil.move(source_path, destination_path)

def check_for_conflict(base_dir):
    for item in os.listdir(base_dir):
        subdir = os.path.join(base_dir, item)
        if os.path.isdir(subdir):
            account_dir = os.path.join(subdir, 'Account')
            saved_vars_dir = os.path.join(subdir, 'SavedVariables')
            if os.path.isdir(account_dir) and os.path.isdir(saved_vars_dir):
                print(f"Conflict found in directory: {subdir}")
                return True
    return False

def get_account_override(base_dir):
    override_file_path = os.path.join(base_dir, '..', 'AccountOverride.txt')
    if os.path.exists(override_file_path):
        with open(override_file_path, 'r') as file:
            return file.readline().strip()  # Read the first line and strip any whitespace
    return None

def main():
    base_dir = '../RawData'
    print(f"Base directory set to: {base_dir}")

    # Delete the Account folder at the start of the script
    account_folder_path = os.path.join(base_dir, 'Account')
    if os.path.exists(account_folder_path):
        shutil.rmtree(account_folder_path)

    print("Checking for directory conflicts...")
    if check_for_conflict(base_dir):
        print("Operation aborted due to directory conflict.")
        return

    move_wtf_contents(base_dir)

    folders = list_folders_in_account(base_dir)

    if folders:
        account_override = get_account_override(base_dir)
        print(f"Available accounts: {folders}")

        if account_override:
            print(f"Account override found: {account_override}")
            if account_override in folders:
                selected_folder = account_override
                print(f"Automatically selected account: {selected_folder}")
                move_contents(selected_folder, base_dir)
            else:
                selected_folder = None
        else:
            selected_folder = None

        if not selected_folder:
            while True:
                try:
                    selection = int(input("Select an account by number: ")) - 1
                    if 0 <= selection < len(folders):
                        selected_folder = folders[selection]
                        print(f"You selected the account: {selected_folder}")
                        move_contents(selected_folder, base_dir)
                        break
                    else:
                        print("Invalid selection. Please enter a number from the list.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
    else:
        print("ERROR: No folders found in the Account directory.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred in the WTF cleaner: {e}")
