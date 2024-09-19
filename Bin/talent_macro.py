import os
import re
import shutil

f=open("Input/DataStore_Talents.lua",'r')
lines=f.readlines()

with open("temp_output.txt",'w') as out:
	flag = None
	p=False
	for line in lines:
		if "Class" in line:
			var_class=line.strip().split('"')[3].strip()
		if "DataStore_TalentsRefDB" in line:
			break
		elif "TalentTrees" in line:
			p=True
		if p:
			out.write(line)

f2=open("temp_output.txt",'r')
lines=f2.readlines()

with open("main_spec.txt",'w') as pri, open("sec_spec.txt",'w') as sec:
	for line in lines:
		if "|" in line.strip():
			#spec=line.split('|')[0].split('"')[1]
			flag=line.split('|')[1].split('"')[0]
		if "nil".casefold() in line:
			continue
		if "}," in line:
			continue
		if "TalentTrees" in line:
			continue
		if "PointsSpent" in line:
			break
		if flag == "1":
			pri.write(line.strip()+"\n")
		if flag == "2":
			sec.write(line.strip()+"\n")

out_macro_file=open("out_macro_talent.txt",'w')

f3=open("main_spec.txt",'r')
lines=f3.readlines()

out_macro_file.write("/click TalentMicroButton"+"\n")
out_macro_file.write("/click GameMenuButtonUIOptions"+"\n")
out_macro_file.write("/click InterfaceOptionsFeaturesPanelPreviewTalentChanges"+"\n")
out_macro_file.write("/click InterfaceOptionsFrameOkay\n")
out_macro_file.write("/click GameMenuButtonContinue\n")
out_macro_file.write("/click PlayerSpecTab1"+"\n")

dict_class={'Blood':1,'Frost':2 ,'Unholy':3,'Balance':1,'Feral':2,'Restoration':3,'Beast Mastery':1,'Marksmanship':2,'Survival':3,'Arcane':1,'Fire':2,'Frost_m':3,'Holy_p':1,'Protection_p':2,'Retribution':3,'Discipline':1,'Holy':2,'Shadow':3,'Assassination':1,'Combat':2,'Subtlety':3,'Elemental':1,'Enhancement':2,'Restoration_s':3,'Affliction':1,'Demonology':2,'Destruction':3,'Arms':1,'Fury':2,'Protection':3}

for line in lines:
	if "|" in line:
		spec=(line.split('|')[0].split('"')[1])
		if spec == "Frost":
			if var_class == "MAGE":
				spec="Frost_m"
		if spec == "Holy":
			if var_class == "PALADIN":
				spec="Holy_p"
		if spec == "Protection":
			if var_class == "PALADIN":
				spec="Protection_p"
		if spec == "Restoration":
			if var_class == "SHAMAN":
				spec="Restoration_s"
		val=dict_class.get(spec)
		out_macro_file.write("/click PlayerTalentFrameTab"+str(val)+"\n")
	if "--" in line.strip():
		value=int(line.split(",")[0])
		ind=line.split('[')[1].split(']')[0]
		for i in range(value):
			out_macro_file.write("/click PlayerTalentFrameTalent"+ind+"\n") 
	if "=" in line.strip() and "," in line.strip():
		value=int(line.split("=")[1].split(",")[0])
		ind=line.split('[')[1].split(']')[0]
		for i in range(value):
			out_macro_file.write("/click PlayerTalentFrameTalent"+ind+"\n")

if os.stat("sec_spec.txt").st_size == 0:
	out_macro_file.write("/click PlayerTalentFrameLearnButton"+"\n")
	out_macro_file.write("/click StaticPopup1Button1\n")
	out_macro_file.write("/click TalentMicroButton\n")

if os.stat("sec_spec.txt").st_size > 0:
	out_macro_file.write("/click TalentMicroButton\n")
	out_macro_file.write("/click PlayerTalentFrameLearnButton"+"\n")
	out_macro_file.write("/click StaticPopup1Button1"+"\n")
	out_macro_file.write(".learn 63644"+"\n")
	#out_macro_file.write(".cheat casttime on"+"\n") #Commented out as it somehow prepends this in the wrong order
	#out_macro_file.write(".cast 63680"+"\n") #This somehow breaks the macro
	out_macro_file.write(".cast 63624"+"\n")
	out_macro_file.write(".cast 63644"+"\n")
	out_macro_file.write("/click TalentMicroButton\n")
	out_macro_file.write("/click PlayerSpecTab2"+"\n")
	f4=open("sec_spec.txt",'r')
	lines=f4.readlines()
	for line in lines:
		if "|" in line:
			spec=(line.split('|')[0].split('"')[1])
			if spec == "Frost":
				if var_class == "MAGE":
					spec="Frost_m"
			if spec == "Holy":
				if var_class == "PALADIN":
					spec="Holy_p"
			if spec == "Protection":
				if var_class == "PALADIN":
					spec="Protection_p"
			if spec == "Restoration":
				if var_class == "SHAMAN":
					spec="Restoration_s"
			val=dict_class.get(spec)
			out_macro_file.write("/click PlayerTalentFrameTab"+str(val)+"\n")
		if "--" in line.strip():
			value=int(line.split(",")[0])
			ind=line.split('[')[1].split(']')[0]
			for i in range(value):
				out_macro_file.write("/click PlayerTalentFrameTalent"+ind+"\n") 
		if "=" in line.strip() and "," in line.strip():
			value=int(line.split("=")[1].split(",")[0])
			ind=line.split('[')[1].split(']')[0]
			for i in range(value):
				out_macro_file.write("/click PlayerTalentFrameTalent"+ind+"\n")
	out_macro_file.write("/click PlayerTalentFrameLearnButton"+"\n")
	out_macro_file.write("/click StaticPopup1Button1\n")
	out_macro_file.write(".cheat casttime off"+"\n")

out_macro_file.close()


def extract_number(line):
    # Use regular expression to find numbers in the line
    numbers = re.findall(r'\d+', line)
    if numbers:
        return int(numbers[-1])  # Return the last number found
    else:
        return float('inf')  # Return a large number if no numbers found

def sort_lines_between_targets(filename):
    target1 = "/click PlayerTalentFrameTab"
    target2 = "/click PlayerTalentFrameLearnButton"

    with open(filename, 'r') as f:
        lines = f.readlines()

    sorted_sections = []
    start_index = 0

    for i in range(len(lines)):
        if target1 in lines[i] or target2 in lines[i] or i == len(lines) - 1:
            if i != start_index:
                # Sort the lines between start_index and i-1 numerically
                sorted_section = sorted(lines[start_index:i], key=extract_number)
                sorted_sections.extend(sorted_section)
            sorted_sections.append(lines[i])  # Append the target line itself
            start_index = i + 1

    return sorted_sections

def split_file(sorted_content):
    split_index = -1
    for i, line in enumerate(sorted_content):
        if ".learn 63644" in line:
            split_index = i
            part1 = sorted_content[:split_index]
            part2 = sorted_content[split_index:]

            with open("../MacroTalentsPrimary.txt", 'w') as file1:
                file1.writelines(part1)
            with open("../MacroTalentsSecondary.txt", 'w') as file2:
                file2.writelines(part2)
            break

    if split_index == -1:
        # Delete files ../MacroTalentsPrimary.txt and ../MacroTalentsSecondary.txt
        if os.path.exists("../MacroTalentsPrimary.txt"):
            os.remove("../MacroTalentsPrimary.txt")
        if os.path.exists("../MacroTalentsSecondary.txt"):
            os.remove("../MacroTalentsSecondary.txt")

        # Copy file outmacrotalent.txt to ../ and rename to MacroTalentsPrimary.txt
        shutil.copyfile("out_macro_talent.txt", "../MacroTalentsPrimary.txt")

# Main script execution
if __name__ == "__main__":
    filename = "out_macro_talent.txt"

    # Step 1: Sort lines between /click PlayerTalentFrameTab or /click PlayerTalentFrameLearnButton
    sorted_content = sort_lines_between_targets(filename)

    # Step 2: Split sorted content based on ".learn 63644" and write to separate files
    split_file(sorted_content)


#os.remove("temp_output.txt") -- Removed as I'm getting processing delays holding up deletion. Deleting in OutputCombiner instead.
