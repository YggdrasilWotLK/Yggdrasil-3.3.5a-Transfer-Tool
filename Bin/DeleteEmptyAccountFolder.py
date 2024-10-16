import os
import shutil

def delete_small_folder(folder_path, size_threshold=1024):
  """Deletes a folder if its total size is less than the specified threshold.

  Args:
    folder_path: The path to the folder to check.
    size_threshold: The minimum size of the folder in bytes to keep it.
  """

  if not os.path.exists(folder_path):
    return  # Folder doesn't exist, do nothing

  total_size = 0
  for root, _, files in os.walk(folder_path):
    for file in files:
      file_path = os.path.join(root, file)
      total_size += os.path.getsize(file_path)

  if total_size < size_threshold:
    shutil.rmtree(folder_path)
    #print(f"Deleted folder: {folder_path}")

# Replace with the actual path to your RawData folder
folder_to_check = "../RawData/Account"
delete_small_folder(folder_to_check)
