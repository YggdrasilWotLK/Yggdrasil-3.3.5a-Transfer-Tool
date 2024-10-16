import glob
import re

# List of achievement IDs to search for
achievement_ids = [6, 7, 8, 9, 10, 14782, 11, 14783, 12, 15805, 13, 19459, 4826, 6193, 9060, 10671, 12544]

# Regular expression pattern to match achievement IDs and completion dates
pattern = r'\[(\d+)\] = (\d+),'

# List to store the results
results = []

# Loop through all files in the Input/CharSplit directory that match the pattern
for filename in glob.glob('Input/CharSplit/DataStore_Achievements_Characters_*.txt'):
    with open(filename, 'r') as f:
        # Loop through each line in the file
        for line in f:
            # Search for the pattern in the line
            match = re.search(pattern, line)
            if match:
                # Extract the achievement ID and completion date
                achievement_id = int(match.group(1))
                completion_date = match.group(2)
                # If the achievement ID is in the list of IDs we're looking for, add it to the results list
                if achievement_id in achievement_ids:
                    results.append(f'{achievement_id}:{completion_date}')

# Write the results to the output file
with open('Output/20-ExpacAchis.txt', 'w') as f:
    for result in results:
        f.write(result + '\n')
