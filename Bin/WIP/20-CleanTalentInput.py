import re

def process_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Pattern to match any content inside curly brackets {}
    pattern = re.compile(r'(\{.*?\})', re.DOTALL)

    # Function to process the content inside the brackets
    def process_content(match):
        # Remove line breaks and tabs
        cleaned_content = match.group(1).replace('\n', '').replace('\t', '')
        # Add new line before every ["name"]
        cleaned_content = re.sub(r'(\[\s*"name"\s*\])', r'\n\1', cleaned_content)
        return cleaned_content
    
    # Remove comments
    content_no_comments = re.sub(r'--.*?(\n|$)', '', content)
    
    # Replace content inside brackets
    modified_content = pattern.sub(process_content, content_no_comments)

    with open(file_path, 'w') as file:
        file.write(modified_content)

# Specify the path to your file
file_path = 'Input/DataStore_TalentData.lua'

# Call the function
process_file(file_path)