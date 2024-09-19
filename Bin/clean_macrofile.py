#Authored by Lortz
import re

f_in=open("CombinedMacroOutput.txt","r")
text=f_in.readlines()
bad_chars=['"','.']
file_out="id_check.txt"
asd=open(file_out,"w")
for line in text:
	if ".send items" and ":" in line:
		temp=re.sub('[A-z]', '', line)
		new_temp=''.join(s for s in temp if not s in bad_chars)
		asd.write("\n".join(re.findall('([0-9]*):',new_temp.strip()))+"\n")
	elif ".send items" in line:
		temp=re.sub('[A-z]', '', line)
		new_temp=''.join(s for s in temp if not s in bad_chars)
		asd.write("\n".join(new_temp.strip().split())+"\n")
	elif ".additem 0" in line:
		pass
	elif ".additem" in line:
		temp=re.sub('[A-z]', '', line)
		new_temp=''.join(s for s in temp if not s in bad_chars)
		asd.write(new_temp.strip().split()[0]+"\n")


with open("ids_item.txt","r") as centry, open("id_check.txt",'r') as susid, open("CombinedMacroOutput_temp.txt",'w') as temp_out, open("CombinedMacroOutput.txt","r") as f_in:
	text=f_in.readlines()
	text2=susid.readlines()
	text3=centry.readlines()
	for line in text2:
		if line not in text3:
			for l2 in text:
				if line.strip() in l2:
					temp_out.write(l2)

with open("CombinedMacroOutput_cleaned.txt","w") as file_out_2, open("CombinedMacroOutput_temp.txt",'r') as temp_out, open("CombinedMacroOutput.txt","r") as f_in:
	text=f_in.readlines()
	text2=temp_out.readlines()
	for line in text:
		if line in text2:
			continue
		else:
			file_out_2.write(line)