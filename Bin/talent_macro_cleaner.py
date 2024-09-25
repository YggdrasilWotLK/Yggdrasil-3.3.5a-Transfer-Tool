#Authored by mostly nick :)
file_path = "../MacroTalentsPrimary.txt"
string_to_remove = ".cast 63624"
lines_to_append = [
    "/click PlayerTalentFrameLearnButton\n",
    "/click StaticPopup1Button1\n"
]

with open(file_path, 'r') as file:
    lines = file.readlines()

modified_lines = [line.replace(string_to_remove, "") for line in lines]

if (len(modified_lines) >= 2 and
    modified_lines[-2].strip() == lines_to_append[0].strip() and
    modified_lines[-1].strip() == lines_to_append[1].strip()):
    pass
else:
    modified_lines.extend(lines_to_append)
    with open(file_path, 'w') as file:
        file.writelines(modified_lines)



