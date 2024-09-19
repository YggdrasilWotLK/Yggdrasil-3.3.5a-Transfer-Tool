#Authored by mostly nick :)
from datetime import datetime

# Define the time spans for each expansion
expansions = {
    "Vanilla": ("01/01/2007", "15/01/2007"),
    "The Burning Crusade": ("16/01/2007", "12/11/2008"),
    "The Wrath of the Lich King": ("13/11/2008", "06/12/2010"),
    "Cataclysm": ("07/12/2010", "24/09/2012"),
    "Mists of Pandaria": ("25/09/2012", "12/11/2014"),
    "Warlords of Draenor": ("13/11/2014", "29/08/2016"),
    "Legion": ("30/08/2016", "13/08/2018"),
    "Battle for Azeroth": ("14/08/2018", "26/10/2020"),
    "Shadowlands": ("27/10/2020", "27/11/2022"),
    "Dragonflight": ("28/11/2022", "23/08/2024"),
    "The War Within": ("24/08/2024", "31/12/9999")
}

# Define the achievements and their corresponding expansions
achievement_expansions = {
    6: "Vanilla",
    7: "Vanilla",
    8: "Vanilla",
    9: "Vanilla",
    10: "Vanilla",
    11: "Vanilla",
    12: "The Burning Crusade",
    13: "The Wrath of the Lich King",
    4826: "Cataclysm",
    6193: "Mists of Pandaria",
    9060: "Warlords of Draenor",
    10671: "Legion",
    12544: "Battle for Azeroth",
    14783: "Shadowlands",
    15805: "Dragonflight",
    19459: "The War Within"
}

# Read the achievements from the file
achievements = {}
with open("Output/20-ExpacAchis.txt", "r") as file:
    for line in file:
        # Split the line on ":" to separate ID and date parts
        ach_id_str, date_str = line.split(":")
        
        # Strip any extra whitespace and convert to integers
        ach_id = int(ach_id_str.strip())
        date = int(date_str.strip())
        
        # Convert the date from yymmdd to a datetime object
        achievements[ach_id] = datetime.strptime(str(date), "%y%m%d")

# Flag to check if at least one achievement is valid
any_valid_achievement = False

# Check the completion date for each achievement and validate it against the corresponding expansion
for ach_id, date in achievements.items():
    exp_name = achievement_expansions.get(ach_id)
    
    if exp_name:
        start, end = expansions[exp_name]
        start_date = datetime.strptime(start, "%d/%m/%Y")
        end_date = datetime.strptime(end, "%d/%m/%Y")
        
        if not any_valid_achievement and start_date <= date <= end_date:
            print(f"Max level achievement ID {ach_id} from retail {exp_name} found! Max level achieved, setting toon level to 80.")
            any_valid_achievement = True
    else:
        print(f"Achievement ID {ach_id} not found in the expansions list.")

# Write to file if at least one achievement is valid
if any_valid_achievement:
    with open("References/5-MaxLevel.txt", "w") as file:
        file.write("79")

import os

# Define the file path
file_path = 'Output/20-ExpacAchis.txt'

# Check if the file exists
if os.path.isfile(file_path):
    try:
        # Delete the file
        os.remove(file_path)
        #print(f"The file '{file_path}' has been deleted successfully.")
    except Exception as e:
        print(f"An error occurred while trying to delete the file: {e}")
else:
    print(f"The file '{file_path}' does not exist.")