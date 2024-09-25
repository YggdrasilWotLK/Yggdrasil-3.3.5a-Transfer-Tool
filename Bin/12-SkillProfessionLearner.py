#Authored by mostly nick :)
def replace_skills(input_file, output_file):
    cooking_mapping = {
        75: "2550",
        150: "3102",
        225: "3413",
        300: "18260",
        375: "33359",
        450: "51296"
    }

    riding_mapping = {
        75: "33388",
        150: "33391",
        225: "34090 \n.learn 54197",
        300: "34091 \n.learn 51497"
    }

    fishing_mapping = {
        75: "7620",
        150: "7731",
        225: "7732",
        300: "18248",
        375: "33095",
        450: "51294"
    }

    first_aid_mapping = {
        75: "3273",
        150: "3274",
        225: "7924",
        300: "10846",
        375: "27028",
        450: "45542"
    }

    alchemy_mapping = {
        75: "2259",
        150: "3101",
        225: "3464",
        300: "11611",
        375: "28596",
        450: "51304"
    }

    blacksmithing_mapping = {
        75: "2018",
        150: "3100",
        225: "3538",
        300: "9785",
        375: "29844",
        450: "51300"
    }

    enchanting_mapping = {
        75: "7411",
        150: "7412",
        225: "7413",
        300: "13920",
        375: "28029",
        450: "51313"
    }

    engineering_mapping = {
        75: "4036",
        150: "4037",
        225: "4038",
        300: "12656",
        375: "30350",
        450: "51306"
    }

    herbalism_mapping = {
        75: "2366",
        150: "2368",
        225: "3570",
        300: "11993",
        375: "28695",
        450: "50300"
    }

    inscription_mapping = {
        75: "45357",
        150: "45358",
        225: "45359",
        300: "45360",
        375: "45361",
        450: "45363"
    }

    jewelcrafting_mapping = {
        75: "25229",
        150: "25230",
        225: "28894",
        300: "28894",
        375: "28897",
        450: "51311"
    }

    leatherworking_mapping = {
        75: "2108",
        150: "3104",
        225: "3811",
        300: "10662",
        375: "32549",
        450: "51302"
    }

    mining_mapping = {
        75: "2575",
        150: "2576",
        225: "3564",
        300: "10248",
        375: "29354",
        450: "50310"
    }

    skinning_mapping = {
        75: "8613",
        150: "8617",
        225: "8618",
        300: "10768",
        375: "32678",
        450: "50305"
    }

    tailoring_mapping = {
        75: "3908",
        150: "3909",
        225: "3910",
        300: "12180",
        375: "26790",
        450: "51309"
    }

    with open(input_file, "r") as input_f:
        lines = input_f.readlines()

    with open(output_file, "w") as output_f:
        for line in lines:
            columns = line.split(", ")
            if columns[0].strip() == "Cooking" and columns[2].strip().isdigit():
                cooking_skill = int(columns[2].strip())
                if cooking_skill in cooking_mapping:
                    output_f.write(f".learn {cooking_mapping[cooking_skill]}\n")
            elif columns[0].strip() == "Riding" and columns[2].strip().isdigit():
                riding_skill = int(columns[2].strip())
                if riding_skill in riding_mapping:
                    output_f.write(f".learn {riding_mapping[riding_skill]}\n")
            elif columns[0].strip() == "Fishing" and columns[2].strip().isdigit():
                fishing_skill = int(columns[2].strip())
                if fishing_skill in fishing_mapping:
                    output_f.write(f".learn {fishing_mapping[fishing_skill]}\n")
            elif columns[0].strip() == "First Aid" and columns[2].strip().isdigit():
                first_aid_skill = int(columns[2].strip())
                if first_aid_skill in first_aid_mapping:
                    output_f.write(f".learn {first_aid_mapping[first_aid_skill]}\n")
            elif columns[0].strip() == "Alchemy" and columns[2].strip().isdigit():
                alchemy_skill = int(columns[2].strip())
                if alchemy_skill in alchemy_mapping:
                    output_f.write(f".learn {alchemy_mapping[alchemy_skill]}\n")
            elif columns[0].strip() == "Blacksmithing" and columns[2].strip().isdigit():
                blacksmithing_skill = int(columns[2].strip())
                if blacksmithing_skill in blacksmithing_mapping:
                    output_f.write(f".learn {blacksmithing_mapping[blacksmithing_skill]}\n")
            elif columns[0].strip() == "Enchanting" and columns[2].strip().isdigit():
                enchanting_skill = int(columns[2].strip())
                if enchanting_skill in enchanting_mapping:
                    output_f.write(f".learn {enchanting_mapping[enchanting_skill]}\n")
            elif columns[0].strip() == "Engineering" and columns[2].strip().isdigit():
                engineering_skill = int(columns[2].strip())
                if engineering_skill in engineering_mapping:
                    output_f.write(f".learn {engineering_mapping[engineering_skill]}\n")
            elif columns[0].strip() == "Herbalism" and columns[2].strip().isdigit():
                herbalism_skill = int(columns[2].strip())
                if herbalism_skill in herbalism_mapping:
                    output_f.write(f".learn {herbalism_mapping[herbalism_skill]}\n")
            elif columns[0].strip() == "Inscription" and columns[2].strip().isdigit():
                inscription_skill = int(columns[2].strip())
                if inscription_skill in inscription_mapping:
                    output_f.write(f".learn {inscription_mapping[inscription_skill]}\n")
            elif columns[0].strip() == "Jewelcrafting" and columns[2].strip().isdigit():
                jewelcrafting_skill = int(columns[2].strip())
                if jewelcrafting_skill in jewelcrafting_mapping:
                    output_f.write(f".learn {jewelcrafting_mapping[jewelcrafting_skill]}\n")
            elif columns[0].strip() == "Leatherworking" and columns[2].strip().isdigit():
                leatherworking_skill = int(columns[2].strip())
                if leatherworking_skill in leatherworking_mapping:
                    output_f.write(f".learn {leatherworking_mapping[leatherworking_skill]}\n")
            elif columns[0].strip() == "Mining" and columns[2].strip().isdigit():
                mining_skill = int(columns[2].strip())
                if mining_skill in mining_mapping:
                    output_f.write(f".learn {mining_mapping[mining_skill]}\n")
            elif columns[0].strip() == "Skinning" and columns[2].strip().isdigit():
                skinning_skill = int(columns[2].strip())
                if skinning_skill in skinning_mapping:
                    output_f.write(f".learn {skinning_mapping[skinning_skill]}\n")
            elif columns[0].strip() == "Tailoring" and columns[2].strip().isdigit():
                tailoring_skill = int(columns[2].strip())
                if tailoring_skill in tailoring_mapping:
                    output_f.write(f".learn {tailoring_mapping[tailoring_skill]}\n")
            elif columns[0].strip() == "Lockpicking" and columns[2].strip().isdigit():
                    output_f.write(f"")
            else:
                output_f.write(line)

input_file = "11-skills.txt"
output_file = "12-skills.txt"

replace_skills(input_file, output_file)