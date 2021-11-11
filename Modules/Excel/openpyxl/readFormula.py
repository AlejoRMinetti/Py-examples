import openpyxl

# read formula example with openpyxl
def readFormula(path):
    wb = openpyxl.load_workbook(path)
    sheet = wb.active
    print(sheet['A2'].value)
    print(sheet['A3'].value)

if __name__ == '__main__':
    readFormula("/home/chama/pythonDev/Py-examples/Modules/Excel/openpyxl/Leer Formula/excelConFormulas.XLSX")