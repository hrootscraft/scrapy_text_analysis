# The following code outputs the URL_IDs which don't have an article
# The Input.csv has articles 44, 57 and 144 as Not found pages
# That is why we have 3 items less in Output.csv

import csv
import json

# Read the URLs from output.json
with open('output.json') as json_file:
    output_data = json.load(json_file)
    output_urls = {item['URL_ID'] for item in output_data}

# Read the URL_ID values from Input.csv
with open('Input.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        url_id = int(row['URL_ID'])
        if url_id not in output_urls:
            print(url_id)
