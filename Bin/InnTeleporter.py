#Authored by mostly nick :)
import os

def create_and_write_file(file_path, text):
  """Creates a file at the specified path and writes the given text to it."""
  try:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Create directories if needed
    with open(file_path, "w") as file:
      file.write(text)
  except Exception as e:
    print(f"Error creating or writing to file: {e}")

if __name__ == "__main__":
  file_path = "Output/Z-Z-InnTeleport.txt"
  text = ".gm visible on\n.tele dalainn\n"
  create_and_write_file(file_path, text)

