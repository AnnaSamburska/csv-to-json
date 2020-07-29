import csv
import json

csvFilePath = './tests_data.csv'
jsonFilePath = 'tests_data.json'

data = {}

csvFile = open(csvFilePath, newline='')

csvReader = csv.DictReader(csvFile)

for row in csvReader:  
    index = row['index']
    if row['report_status'] == 'True':
        row['report_status'] = True
    else:
        row['report_status'] = False
    data[index] = row


with open(jsonFilePath, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent = 4))
