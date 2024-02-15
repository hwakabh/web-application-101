import yaml


with open('./companies.yaml', 'r') as f:
    c = f.read()

companies = yaml.safe_load(c)

print(companies['companies'][3])
