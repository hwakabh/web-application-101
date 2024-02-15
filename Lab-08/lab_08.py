companies = ["Amazon", "Google", "Microsoft", "VMware"]

print(companies)
print()

print(companies[1])
print()

# # IndexError
# print(companies[100])
# print()

companies.append('Apple')
print(companies)
# print()

for c in companies:
    print(f"Name: {c}")
