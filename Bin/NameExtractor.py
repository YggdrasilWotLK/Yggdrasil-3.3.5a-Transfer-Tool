#Authored by mostly nick :)
import os
import re

def read_file_safely(file_path):
    """Reads the file content safely, handling potential decoding errors."""
    content = []
    with open(file_path, 'rb') as file:
        for line in file:
            try:
                content.append(line.decode('utf-8'))
            except UnicodeDecodeError:
                content.append('')  # Add an empty line for lines that can't be decoded
    return ''.join(content)

def write_file_safely(file_path, content):
    """Writes content to a file, ignoring encoding errors."""
    with open(file_path, 'wb') as file:
        file.write(content.encode('utf-8', errors='ignore'))

def get_character_names_and_realms(file_path):
    """Extracts character names and realms from the Lua file."""
    content = read_file_safely(file_path)

    # Pattern for 'profileKeys' mapping
    profile_keys_pattern = r'\["profileKeys"\]\s*=\s*\{([^}]*)\}'
    profile_keys_matches = re.findall(profile_keys_pattern, content, re.DOTALL)
    
    # Pattern for 'global' character definitions
    global_chars_pattern = r'\["Default\.(.*?)\.(.*?)"\]\s*=\s*\{[^}]*\["name"\]\s*=\s*"(.*?)"'
    global_chars_matches = re.findall(global_chars_pattern, content)

    results = {}
    
    # Extract data from profileKeys matches
    for match in profile_keys_matches:
        pairs = re.findall(r'\["(.*?)"\]\s*=\s*"(.*?)"', match)
        for key, value in pairs:
            parts = key.split(' - ')
            if len(parts) == 3:
                char_name = parts[0]
                realm = ' - '.join(parts[1:])  # Realm
                if char_name not in results:
                    results[char_name] = (realm, value)

    # Extract data from global characters matches
    for realm, char_name, display_name in global_chars_matches:
        if char_name not in results:
            results[char_name] = (realm, display_name)

    return results

def write_to_file(name):
    """Writes the selected character name to a file."""
    os.makedirs('References', exist_ok=True)
    with open('References/Argument.txt', 'w') as file:
        file.write(name)

def update_lua_files(raw_data_path, selected_name, selected_realm):
    """Updates Lua files to remove/rename non-selected realm entries."""
    for root, _, files in os.walk(raw_data_path):
        for file in files:
            if file.endswith(".lua"):
                file_path = os.path.join(root, file)
                content = read_file_safely(file_path)

                # Update non-selected realms
                content = re.sub(rf'\["Default\.(?!{selected_realm})(.*?)\.{selected_name}"\]', '["Default.\\1.DELETEDNAME"]', content)
                content = re.sub(rf'\["{selected_name} - (?!{selected_realm})(.*?)"\]', '["DELETEDNAME - \\1"]', content)

                write_file_safely(file_path, content)

def main():
    """Main function to handle user interaction and file updates."""
    raw_data_path = "../RawData"
    lua_file = "DataStore_Characters.lua"
    file_path = os.path.join(raw_data_path, lua_file)

    try:
        characters = get_character_names_and_realms(file_path)
        if not characters:
            raise FileNotFoundError

        if len(characters) > 1:
            print("Character names found:")
            for i, (name, _) in enumerate(characters.items(), 1):
                print(f"{i}. {name}")

            while True:
                selection = input("Select character name by number: ")
                try:
                    index = int(selection) - 1
                    if 0 <= index < len(characters):
                        selected_name = list(characters.keys())[index]
                        break
                    else:
                        print("Invalid selection. Please try again.")
                except ValueError:
                    print("Please enter a valid number.")

        elif len(characters) == 1:
            selected_name = list(characters.keys())[0]

        selected_realm = characters[selected_name][0]

        write_to_file(selected_name)
        print(f"Character identified: {selected_name} - {selected_realm}. Extracting character files...")

        update_lua_files(raw_data_path, selected_name, selected_realm)

    except FileNotFoundError:
        print(f"ERROR: No characters found, terminating! Were the transfer addons correctly set up?")
        input("Press Enter to exit...")
        parent_pid = os.getppid()
        os.kill(parent_pid, 9)
    except Exception as e:
        print(f"CRITICAL ERROR: {e}. Terminating!")
        input("Press Enter to exit...")
        parent_pid = os.getppid()
        os.kill(parent_pid, 9)

if __name__ == "__main__":
    main()
