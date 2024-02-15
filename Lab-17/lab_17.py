import openpyxl


f = openpyxl.load_workbook('./Locker.xlsx')

# Listing Excel sheets
print(f.sheetnames)

s = f['16F\u3000Locker']

# Specify Cell number
name = s['I12'].value

print(name)
