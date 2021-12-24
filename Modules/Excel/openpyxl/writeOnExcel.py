# importamos el submodulo "Workbook"
from openpyxl import load_workbook

# especificamos el nombre y la ruta del archivo
filesheet = "./demosheet.xlsx"

# creamos el objeto load_workbook
wb = load_workbook(filesheet)

# Seleccionamos el archivo
sheet = wb.active

# Ingresamos el valor 56 en la celda 'A1'
sheet['C2'] = 56

# Ingresamos el valor 1845 en la celda 'B3'
sheet['C4'] = 1845

# Guardamos el archivo con los cambios
wb.save(filesheet)