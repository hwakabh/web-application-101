import csv


# read .csv file reader()
with open('./companies.csv', 'r') as f:
    # csv.reader() returns type: csv.reader object
    # <class '_csv.reader'>
    rows = csv.reader(f)

    for r in rows:
        print(r[6])
