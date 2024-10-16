import re
import os

def extract_link_numbers(input_filename, output_filename):
    # Check if Recipient.txt exists and has content
    if os.path.exists('References/Recipient.txt'):
        with open('References/Recipient.txt', 'r') as player_file:
            playername = player_file.read().strip()
        
        if not playername:
            playername = input("Please enter the player name: ").strip()
            with open('References/Recipient.txt', 'w') as player_file:
                player_file.write(playername)
                print(f"Player name '{playername}' written to References/Recipient.txt.")
    else:
        playername = input("Please enter the player name: ").strip()
        with open('References/Recipient.txt', 'w') as player_file:
            player_file.write(playername)
            print(f"Player name '{playername}' written to References/Recipient.txt.")

    with open(input_filename, 'r') as file:
        lines = file.readlines()
    
    pattern = r'\|Hitem:(\d{5}):'
    matches = []

    for line in lines:
        if '["link"]' in line:
            match = re.search(pattern, line)
            if match:
                matches.append(match.group(1))
    
    with open(output_filename, 'w') as file:
        for i in range(0, len(matches), 12):
            items = ' '.join(matches[i:i+12])
            file.write(f'.send items {playername} "Bags" "Bags" {items}\n')

# Use the function
input_filename = 'Input/DataStore_Containers.lua'
output_filename = 'Output/BagIDs.txt'
extract_link_numbers(input_filename, output_filename)

#print(f"Extracted numbers have been written to {output_filename}")
