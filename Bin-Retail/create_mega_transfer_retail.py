#Authored by mostly nick :)
file_input=open("0_Run.bat",'r')
file_output=open("mega_transfer_retail.py",'w')
text=file_input.readlines()
script=[]

for line in text:
	if "PYTHON" in line:
			script.append(line.split()[1])

imp_list=[]

for s in script:
	sl=open(s,'r')
	out=sl.readlines()
	for line_2 in out:
			if "import" in line_2:
				imp_list.append(line_2)

imp_list=sorted(set(imp_list))

i=0
while i < len(imp_list):
	file_output.write(imp_list[i])
	i+=1

for s in script:
	sl=open(s,'r')
	out=sl.readlines()
	file_output.write("\n")
	for line_2 in out:
		if "import" in line_2:
			continue
		else:
			file_output.write(line_2)
