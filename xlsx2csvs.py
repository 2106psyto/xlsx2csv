import openpyxl
import os
import csv


def value(prop):
    return prop.value

wb = openpyxl.load_workbook('test.xlsx', read_only=True)
sheets = wb.worksheets

for sheet in sheets:
    name = sheet.title
    with open('{}_{}.csv'.format('test.xlsx', name), 'w', newline='') as w:
        writer = csv.writer(w)
        rows = sheet.rows
        for row in rows:
            row_in_csv = list(map(value, row))
            print(row_in_csv)
            writer.writerow(row_in_csv)