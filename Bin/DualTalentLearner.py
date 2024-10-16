with open('Output/AchievementGranter.txt', 'r') as input_file:
    # Read all lines from the file
    lines = input_file.readlines()

with open('Output/X0-DualSpecialization.txt', 'w') as output_file:
    # Iterate through each line in the input file
    for line in lines:
        # Check if the line contains the number 2716
        if '2716' in line:
            # If it does, write the desired output to the output file
            output_file.write(".cast 63680\n.cast 63624\n")
            break  # Stop searching after finding the first occurrence

#print("Dual Talent Specialization captured.")