import os
import shutil

def move_wtf_contents(base_dir):
    wtf_dir = os.path.join(base_dir, 'WTF')
    
    if os.path.exists(wtf_dir) and os.path.isdir(wtf_dir):
        items = os.listdir(wtf_dir)
        
        for item in items:
            source_path = os.path.join(wtf_dir, item)
            destination_path = os.path.join(base_dir, item)
            
            shutil.move(source_path, destination_path)
        
        os.rmdir(wtf_dir)

def list_folders_in_account(base_dir):
    account_dir = os.path.join(base_dir, 'account')
    
    if os.path.exists(account_dir) and os.path.isdir(account_dir):
        items = os.listdir(account_dir)
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
        return []

def move_contents(selected_folder, base_dir):
    source_dir = os.path.join(base_dir, 'account', selected_folder)
    
    if os.path.exists(source_dir) and os.path.isdir(source_dir):
        items = os.listdir(source_dir)
        
        for item in items:
            source_path = os.path.join(source_dir, item)
            destination_path = os.path.join(base_dir, item)
            
            shutil.move(source_path, destination_path)

def check_for_conflict(base_dir):
    for item in os.listdir(base_dir):
        subdir = os.path.join(base_dir, item)
        if os.path.isdir(subdir):
            account_dir = os.path.join(subdir, 'account')
            saved_vars_dir = os.path.join(subdir, 'SavedVariables')
            if os.path.isdir(account_dir) and os.path.isdir(saved_vars_dir):
                print(f"Conflict found in directory: {subdir}")
                return True
    return False

def main():
    base_dir = '../RawData'

    if check_for_conflict(base_dir):
        print("Operation aborted due to directory conflict.")
        return

    move_wtf_contents(base_dir)
    folders = list_folders_in_account(base_dir)
    
    if folders:
        while True:
            try:
                selection = int(input("Select an account by number: ")) - 1
                if 0 <= selection < len(folders):
                    selected_folder = folders[selection]
                    move_contents(selected_folder, base_dir)
                    break
                else:
                    print("Invalid selection. Please enter a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
