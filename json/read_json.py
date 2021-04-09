import json
import os
import re

base_path = 'insert path to the json file - we will pretend we are using data from facebook'
json_files = []
p = re.compile(".*\.json")

with open('translated_facebook_data.txt', 'w') as output:
    for (root, dirs, files) in os.walk(base_path):
        for each in files:
             if re.search(p, each):
                 temp = os.path.join(root, each)
                 f = open(temp)
                 data = json.load(f)
                 formatted_data = json.dumps(data, indent=2, sort_keys=True)
                 output.write(formatted_data)
                 output.write('\n')
output.close()

