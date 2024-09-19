#Authored by mostly nick :)
import os
import shutil

def read_character_name(file_path):
  """Reads the character name from the specified file."""
  try:
    with open(file_path, "r") as file:
      character_name = file.readline().strip()
      return character_name
  except FileNotFoundError:
    return None
  except Exception as e:
    return None

def search_and_copy_valid_files(character_name):
    raw_folder = "../RawData"
    found_file = False
    for root, dirs, files in os.walk(raw_folder):
        for file in files:
            if file == "EveryQuest.lua":
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    if "EveryQuestDBPC" in content and character_name in content:
                        destination = os.path.join(raw_folder, "EveryQuestData.lua")
                        if not os.path.exists(destination) or os.path.getsize(file_path) != os.path.getsize(destination):
                            shutil.copyfile(file_path, destination)
                            found_file = True
                            break
        if found_file:
            break
    return found_file
    
def main():
    character_name_file = "References/Argument.txt"
    character_name = read_character_name(character_name_file)
    if character_name:
        found_valid_file = search_and_copy_valid_files(character_name)
        if not found_valid_file:
            # Check for EveryQuestData.lua in ../RawData
            if not os.path.exists("../RawData/EveryQuestData.lua"):
                print("ALERT: Did not find EveryQuests file for character. Ignore me if you're not transferring quests..")

    else: 
        pass

if __name__ == "__main__":
  main()
