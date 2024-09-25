#Authored by mostly nick :)
import csv
import os
import shutil

def compare_and_replace():
    # Read GlyphCount.txt
    with open('GlyphCount.txt', 'r') as glyph_file:
        glyph_lines = glyph_file.readlines()

    # Read ItemID_full.txt
    with open('References/ItemID_full.txt', 'r') as item_file:
        item_reader = csv.reader(item_file)
        item_data = list(item_reader)

    # Read playername from Recipient.txt
    with open('References/Recipient.txt', 'r') as args_file:
        playername = args_file.readline().strip()

    # Iterate through each line in GlyphCount.txt
    for i, glyph_line in enumerate(glyph_lines):
        # Get the text before the colon
        glyph_text = glyph_line.split(':')[0].strip()

        # Iterate through each row in ItemID_full.txt
        for item_row in item_data:
            # Get the text between the 4th and 5th commas
            item_text = item_row[4].strip()

            # If there's a match
            if glyph_text.casefold() == item_text.casefold():
                # Replace the matching text in GlyphCount.txt with the number from the first column of ItemID_full.txt
                glyph_lines[i] = glyph_lines[i].replace(glyph_text, item_row[0])

    # Write the modified content back to GlyphCount.txt with spaces at the end of each line
    with open('GlyphCount.txt', 'w') as glyph_file:
        for line in glyph_lines:
            glyph_file.write(line.rstrip() + ' ')

    # Prefix each line with '.send items playername'
    with open('GlyphCount.txt', 'r') as glyph_file:
        modified_lines = glyph_file.readlines()

    with open('GlyphCount.txt', 'w') as glyph_file:
        for line in modified_lines:
            glyph_file.write(f'.send items {playername} "Glyphs" "Glyphs" {line}')

    # Copy GlyphCount.txt to the output folder and rename it to GlyphMacro.txt
    shutil.copy('GlyphCount.txt', 'output/GlyphMacro.txt')

    # Delete GlyphCount.txt, GlyphSpellID.txt, and GlyphName.txt
    os.remove('GlyphCount.txt')
    os.remove('GlyphSpellID.txt')
    os.remove('GlyphName.txt')

if __name__ == "__main__":
    compare_and_replace()
