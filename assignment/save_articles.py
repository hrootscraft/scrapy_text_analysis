# Following file saves the articles in a txt file

import json
import os

# Read the URLs from output.json
with open('output.json') as json_file:
    output_data = json.load(json_file)

# Create the folder if it doesn't exist
folder_path = 'article_texts'
os.makedirs(folder_path, exist_ok=True)

# Loop through output_data and save text files
for item in output_data:
    url_id = item['URL_ID']
    body_text = item['body']

    # Create the text file
    filename = f"{url_id}.txt"
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'w') as text_file:
        text_file.write(body_text)
