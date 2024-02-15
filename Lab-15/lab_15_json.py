import json


# read .json file with load()
with open('./companies.json', 'r') as f:
    companies = json.load(f)

# json.load() returns type: dict
print(companies['VMW'])
