import csv
import json
import requests

try:
    data = []

    with open("data.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    print("JSON Data:")
    print(json.dumps(data))

    url = "https://example.com/api" #test library
    response = requests.post(url, json=data)

except:
    print("Error reading file or sending data.")
