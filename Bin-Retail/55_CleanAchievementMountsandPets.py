def modify_file_in_place(file_path, skip_numbers):
  """Modifies a file in place by removing lines containing specified numbers.

  Args:
    file_path: The path to the file to modify.
    skip_numbers: A set of numbers to filter out.
  """

  with open(file_path, 'r+') as file:
    lines = file.readlines()
    file.seek(0)  # Move the file pointer to the beginning
    file.truncate()  # Clear the file contents

    for line in lines:
      if not any(number in line for number in skip_numbers):
        file.write(line)

# Example usage
skip_numbers = {
    '70613', '69002', '61773', '44841', '44842', '44843',
    '60025', '59961', '40990', '68187', '68188', '60119',
    '60118', '72808', '72807', '63956', '63963', '60024',
    '61472'
}

input_file = 'Output/54-MountsAndPetsMacro.txt'
modify_file_in_place(input_file, skip_numbers)