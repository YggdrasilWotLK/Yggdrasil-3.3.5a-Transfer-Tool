# Read GlyphName.txt
with open('GlyphName.txt', 'r', encoding='utf-8') as glyph_file:
    glyph_lines = glyph_file.readlines()

# Extract glyph names from GlyphName.txt
glyph_names = [line.strip() for line in glyph_lines]

# Create a dictionary to store glyph names and their occurrences
glyph_occurrences = {}

# Count occurrences of each glyph in GlyphName.txt
for glyph_name in glyph_names:
    if glyph_name in glyph_occurrences:
        glyph_occurrences[glyph_name] += 1
    else:
        glyph_occurrences[glyph_name] = 1

# Write occurrences of each glyph to GlyphCount.txt
with open('GlyphCount.txt', 'w', encoding='utf-8') as count_file:
    for glyph_name, occurrences in glyph_occurrences.items():
        count_file.write(f"{glyph_name}:{occurrences}\n")

# Print occurrences of each glyph
for glyph_name, occurrences in glyph_occurrences.items():
    print(f"Occurrences of '{glyph_name}': {occurrences}")
