import os

def find_lua_file(filename):
  if os.path.isfile(filename):
    return filename
  else:
    return None

def remove_line_breaks_and_tabs(filename):
  with open(filename, 'r') as f:
    content = f.read()

  modified_content = content.replace('{\n', '{').replace('\t', '')

  with open('tempquest.txt', 'w') as f:
    f.write(modified_content)

lua_file = find_lua_file('Raw/EveryQuestData.lua')

if lua_file:
  remove_line_breaks_and_tabs(lua_file)
else:
  print("ERROR: EveryQuestData.lua not found. Please check that file is present if transferring quest progress.")
