import re

def extract_numbers(input_file, output_file):
    """
    Extracts all numbers from each line of a file, filtering out first, last, and values above 99999, reverses the order, separates them with colon (:), prefixes each line with '.additem', and writes non-empty lines without ':0' to another file.

    Args:
        input_file: Path to the file containing the data.
        output_file: Path to the file where the filtered and reversed numbers will be written.
    """
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            # Use regular expression to find one or more digits (\d+)
            numbers = re.findall(r'\d+', line)
            # Filter out first and last values (slice from index 1 to -1)
            filtered_numbers = numbers[1:-1]
            # Filter out numbers above 99999
            filtered_numbers = [num for num in filtered_numbers if int(num) <= 99999]
            # Filter out the number 37742
            filtered_numbers = [num for num in filtered_numbers if num != '37742']
            # Reverse the order of filtered numbers
            filtered_numbers.reverse()
            # Join filtered numbers with colon (:)
            joined_numbers = " ".join(filtered_numbers)
            # Check if the line doesn't contain ":0" and write if not empty
            if filtered_numbers and ":0" not in joined_numbers:
                f_out.write(".additem " + joined_numbers + "\n")
        # Append .additem 0 -99 to the end of the output
        f_out.write(".additem 0 -99\n")
        f_out.write(".additem 37742 -9999\n")

if __name__ == "__main__":
    input_file = "Input/DataStore_Currencies.lua"
    output_file = "Output/CurrencyOutput.txt"
    extract_numbers(input_file, output_file)