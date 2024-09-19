import os

def replace_lines(input_file, output_file):
    # Define the mapping of words to numbers
    replacement_mapping = {
        "Two-Handed Maces": "160",
        "Mail": "413",
        "Swords": "43",
        "Axes": "44",
        "Fist Weapons": "473",
        "Unarmed": "162",
        "Plate Mail": "293",
        "Plate": "293",
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
        "Defense": "95"
    }

    # Open input file for reading
    with open(input_file, "r") as input_f:
        lines = input_f.readlines()

    # Open output file for writing
    with open(output_file, "w") as output_f:
        # Iterate through each line
        for line in lines:
            # Split the line into columns
            columns = line.split(", ")

            # Check if the first column is in the replacement mapping
            if columns[0].strip() in replacement_mapping:
                # Skip this line if it matches any skill in the replacement mapping
                continue

            # Write the original line to the output file
            output_f.write(line)

    # Delete the input file
    os.remove(input_file)
    # Move the output file to the Output folder
    os.replace(output_file, os.path.join("Output", output_file))

# Paths to input and output files
input_file = "12-skills.txt"
output_file = "SkillSpellIDMacro.txt"

# Call the function to replace lines with specified strings before the colon and delete the "Defense" line
replace_lines(input_file, output_file)

#print("Skills with no Spell ID cleaned from macro.")