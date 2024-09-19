#Authored by mostly nick :)
import csv

def match_columns(glyph_file, reference_file, output_file):
    # Read the reference file into a dictionary with column 1 as key and column 137 as value
    references = {}
    with open(reference_file, 'r') as ref_file:
        ref_reader = csv.reader(ref_file, delimiter=',')
        for row in ref_reader:
            if row:  # Check if the row is non-empty
                references[row[0]] = row[136]

    # Match column 1 in glyph file with the dictionary and write the corresponding value to output file
    with open(glyph_file, 'r') as glyph_f, open(output_file, 'w', newline='') as output_f:
        glyph_reader = csv.reader(glyph_f, delimiter=',')
        output_writer = csv.writer(output_f, delimiter=',')
        
        for row in glyph_reader:
            if row:  # Check if the row is non-empty
                glyph_id = row[0]
                if glyph_id in references:
                    output_writer.writerow([references[glyph_id]])
                else:
                    output_writer.writerow([])  # Write an empty row if no match found

# Example usage:
match_columns('GlyphSpellID.txt', 'References/Spell.txt', 'GlyphName.txt')
