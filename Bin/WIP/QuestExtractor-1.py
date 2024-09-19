#Authored by mostly nick :)
import os

def find_lua_file(start_dir):
    for root, dirs, files in os.walk(start_dir):
        if 'Raw' in dirs and 'EverQuest.lua' in files:
            return os.path.join(root, 'Raw', 'EverQuest.lua')
    return None

def remove_line_breaks_and_tabs(filename):
    with open(filename, 'r') as f:
        content = f.read()

    modified_content = content.replace('{\n', '{').replace('\t', '')

    with open('tempquest.txt', 'w') as f:
        f.write(modified_content)

lua_file = find_lua_file('.')
if lua_file:
    remove_line_breaks_and_tabs(lua_file)
    print("Processed:", lua_file)
else:
    print("EverQuest.lua not found in any subdirectory under the current directory.")