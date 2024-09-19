#Authored by mostly nick :)
import os

# Define file paths
input_file = 'Output/22-AchievementMacro.txt'
output_file = 'Output/90-ProfessionPayment.txt'

# Delete output file if it exists
if os.path.exists(output_file):
    os.remove(output_file)

# Check if input file exists
if not os.path.exists(input_file):
    print(f"ALERT: Achivement file error!")
else:
    # Read the input file
    with open(input_file, 'r') as file:
        content = file.read()

    # Determine the conditions based on file content
    contains_735 = '.achievement add 735' in content
    contains_734 = '.achievement add 734' in content

    # Prepare the output based on conditions
    if contains_735:
        output_content = (
            '.send items Charactername "Professions" "Hi! We see that you had two Grand Master professions previously. In order to select your new profession here, please find the enclosed emblems. You can exchange these at the Mall\'s Scientist to get two 450/450 professions of your choosing." 49426:200\n'
        )
        print("")
        print("Professions status:")
        print(f"Two professions found! Compensation to buy new professions written to to {output_file}")
        print("")
    elif contains_734 and not contains_735:
        output_content = (
            '.send items Charactername "Professions" "Hi! We see that you had one Grand Master profession previously. In order to select your new professions here, please find the enclosed emblems. You can exchange these at the Mall\'s Scientist to get a 450/450 profession of your choosing." 49426:100\n'
        )
        print("")
        print("Professions status:")
        print(f"One profession found! Compensation to buy new profession written to to {output_file}")
        print("")
    else:
        output_content = ''

    # Write to the output file
    if output_content:
        with open(output_file, 'w') as file:
            file.write(output_content)
    else:
        print("")
        print("Professions status:")
        print("Character has no maxed professions - skipping profession macro.")
        print("")
