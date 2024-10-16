import re

def read_lua_file(file_path):
    """Reads the content of a LUA file."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def extract_achievement_ids(lines):
    """Extracts achievement IDs from lines containing 'true'."""
    achievement_ids = []
    for line in lines:
        if "true" in line:
            match = re.search(r'\b(\d+)', line)
            if match:
                achievement_ids.append(match.group(1))
    return achievement_ids

def write_achievement_commands(achievement_ids, output_file, excluded_ids):
    """Writes sorted achievement add commands to the output file, excluding specific IDs."""
    with open(output_file, 'w') as file:
        for achievement_id in sorted(achievement_ids, key=int):
            if achievement_id not in excluded_ids:
                file.write(f".achievement add {achievement_id}\n")

def main():
    input_file = 'Input/DataStore_Achievements.lua'
    output_file = 'Output/AchievementGranter.txt'
    excluded_ids = {str(i) for i in range(1, 14)}  # IDs to exclude

    #print(f"Reading LUA file: {input_file}")
    lines = read_lua_file(input_file)
    #print("Extracting achievement IDs...")
    
    achievement_ids = extract_achievement_ids(lines)
    #print(f"Found {len(achievement_ids)} achievements to add.")

    #print(f"Writing sorted achievement add commands to '{output_file}'...")
    write_achievement_commands(achievement_ids, output_file, excluded_ids)
    #print("Achievement add commands have been written to the output file.")
    #print("Processing complete.")

if __name__ == '__main__':
    main()
