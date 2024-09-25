#Authored by mostly nick :)
import os

# Skill mapping dictionary containing profession names as keys and skill IDs as values
skill_mapping = {
    "Two-Handed Maces": "160",
    "Mail": "413",
    "Swords": "43",
    "Axes": "44",
    "Fist Weapons": "473",
    "Unarmed": "162",
    "Plate Mail": "293",
    "Thrown": "176",
    "Poisons": "40",
    "Shield": "433",
    "Dual Wield": "118",
    "Polearms": "229",
    "Two-Handed Swords": "55",
    "Two-Handed Axes": "172",
    "Guns": "46",
    "Runeforging": "776",
    "Staves": "136",
    "Crossbows": "226",
    "Maces": "54",
    "Wands": "228",
    "Daggers": "173",
    "Protection": "267",
    "Swimming": "155",
    "Bows": "45",
    "Frost": "771",
    "Alchemy": "171",
    "Blacksmithing": "164",
    "Enchanting": "333",
    "Engineering": "202",
    "Herbalism": "182",
    "Inscription": "773",
    "Jewelcrafting": "755",
    "Leatherworking": "165",
    "Mining": "186",
    "Skinning": "393",
    "Tailoring": "197",
    "Cooking": "185",
    "Fishing": "356",
    "Riding": "762",
    "First Aid": "129",
    "Lockpicking": "633",
    "Defense": "95"
}

def replace_professions(input_file, output_file):
    with open(input_file, "r") as input_f:
        lines = input_f.readlines()

    with open(output_file, "w") as output_f:
        for line in lines:
            columns = line.split(", ")
            if columns[0].strip() in skill_mapping:
                skill_id = skill_mapping[columns[0].strip()]
                output_f.write(f".setskill {skill_id} {columns[1].strip()}\n")
            else:
                output_f.write(line)

    # Delete the input files after processing
    os.remove(input_file)

# Paths to input and output files
input_file = "11-skills.txt"
output_file = "Output/SkillLevels.txt"

# Call the function to replace profession names with skill IDs
replace_professions(input_file, output_file)

#print("Profession names replaced with corresponding Skill IDs.")

# Delete the remaining input file
os.remove("10-skills.txt")
