import re

def extract_info(line):
    name_match = re.search(r'\["name"\] = "([^"]+)"', line)
    rank_match = re.search(r'\["rank"\] = (\d+)', line)
    
    if name_match and rank_match:
        name = name_match.group(1)
        rank = rank_match.group(1)
        return f"{name},{rank}"
    return None

# Read content from a file
file_path = 'Input/DataStore_TalentData.lua'
with open(file_path, 'r') as file:
    lines = file.readlines()

results = []

for line in lines:
    if '["primary"]' in line:
        results.append('--primary')
    elif '["secondary"]' in line:
        results.append('--secondary')
    else:
        info = extract_info(line)
        if info and not info.endswith(',0'):
            results.append(info)

# Write the results to a file
output_file_path = 'talenttemp1.txt'
with open(output_file_path, 'w') as output_file:
    for result in results:
        output_file.write(result + '\n')

#print(f"Results written to {output_file_path}")
