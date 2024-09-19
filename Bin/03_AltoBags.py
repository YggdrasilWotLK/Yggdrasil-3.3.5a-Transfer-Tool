#Authored by mostly nick :)
def compare_files(file1, file2, output_file):
    # Reading the first file into a dictionary
    preppedcount2 = {}
    with open(file1, 'r') as f:
        for line in f:
            if "," in line:
                col1, col2 = line.strip().split(',')
                preppedcount2[col2] = col1
            else:
                continue
    
    with open(file2, 'r') as f, open(output_file, 'w') as out:
        for line in f:
            if "," in line:
                col1, col2 = line.strip().split(',')
            else:
                continue
            
            if col2 in preppedcount2:
                out.write(f"{col1}:{preppedcount2[col2]}\n")
            else:
                out.write(f"{col1}:1\n")

# Usage
compare_files('preppedcount2.txt', 'prepped3.txt', 'ItemOutput.txt')
