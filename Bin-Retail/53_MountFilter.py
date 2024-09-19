#Authored by mostly nick :)
# Define file paths
mount_spell_ids_file = '52-MountSpellIDs.txt'
allowed_mounts_file = 'Resources/AllowedMounts.txt'

# Read allowed mounts from AllowedMounts.txt
with open(allowed_mounts_file, 'r') as f:
    allowed_mounts = set(line.strip() for line in f)

# Read and filter mount spell IDs
with open(mount_spell_ids_file, 'r') as f:
    lines = f.readlines()

# Filter lines where the number is in allowed_mounts
filtered_lines = [line for line in lines if line.strip() in allowed_mounts]

# Write the filtered lines back to 52-MountSpellIDs.txt
with open(mount_spell_ids_file, 'w') as f:
    f.writelines(filtered_lines)

print("Filtering complete. Invalid mounts and pets removed.")
