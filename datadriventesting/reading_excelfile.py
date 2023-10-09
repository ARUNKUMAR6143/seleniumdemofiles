import openpyxl


file = "C:\\Users\lenovo\Downloads\\python.xlsx"
workbook = openpyxl.load_workbook(file)


#sheet = workbook['sheet1']
try:
    sheet = workbook['sheet1']
    # Now you can work with the 'sheet' object
except KeyError as e:
    print(f"Worksheet 'sheet1' does not exist in the workbook.")
rows = sheet.max_rows
cols = sheet.max_columns

for r in range(1,rows+1):
    for c in range(1,cols):
        print(sheet.cell(r,c).value)



