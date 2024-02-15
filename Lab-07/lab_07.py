companies = {
    "VMW": "VMware",
    "GOOG": "Google",
    "AAPL": "Apple",
    "AMZN": "Amazon",
    "MSFT": "Microsoft"
}

print(companies)
print()

print(companies["GOOG"])
print(companies.get('GOOG'))
print()

# # KeyError
# print(companies["DELL"])

companies['DELL'] = 'Dell Technologies'
print(companies)
print()

print(companies.keys())
print(companies.values())
print(companies.items())
