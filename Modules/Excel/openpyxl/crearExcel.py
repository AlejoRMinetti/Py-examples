# importamos el submodulo "Workbook"
from openpyxl import Workbook

# creamos el objeto Workbook
wb = Workbook()

# especificamos el nombre y la ruta del archivo
filesheet = "./demosheet.xlsx"

# guardamos el archivo
wb.save(filesheet)