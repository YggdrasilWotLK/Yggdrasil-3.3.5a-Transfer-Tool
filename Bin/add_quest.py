#Authored by Lortz
with open("Output/2-macro_quests.txt",'w') as out, open("Input/DataStore_Quests.lua","r") as fi:
	text=fi.readlines()
	for line in text:
		if "Hquest:" in line:
			out.write(".quest add " + line.split(":")[1]+"\n")
