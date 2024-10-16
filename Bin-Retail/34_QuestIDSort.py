# Filename of the file to sort
filename = '33-QuestIDs.txt'

def sort_file_numerically(filename):
    try:
        # Read the file
        with open(filename, 'r') as file:
            # Read all lines and strip any extra whitespace
            lines = [line.strip() for line in file if line.strip()]

        # Convert lines to integers, ignoring any non-numeric lines
        numbers = []
        for line in lines:
            try:
                number = int(line)
                numbers.append(number)
            except ValueError:
                # Skip lines that cannot be converted to integers
                continue

        # Sort numbers numerically
        numbers.sort()

        # Write the sorted numbers back to the file
        with open(filename, 'w') as file:
            for number in numbers:
                file.write(f"{number}\n")

        #print(f"File '{filename}' has been sorted numerically.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function to sort the file
sort_file_numerically(filename)
