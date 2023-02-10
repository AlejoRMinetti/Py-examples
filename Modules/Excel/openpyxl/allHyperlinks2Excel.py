import os
import openpyxl

def write_hyperlinks_to_excel(directory_path, excel_file_path):
    # Get all the files and directories in the directory
    items = os.listdir(directory_path)
    
    # Create a workbook
    workbook = openpyxl.Workbook()
    
    # Get the active worksheet
    worksheet = workbook.active
    
    # Write the header
    worksheet['A1'] = "File/Directory Name"
    worksheet['B1'] = "Hyperlink"
    
    row = 2
    for item in items:
        item_path = os.path.join(directory_path, item)
        if os.path.isfile(item_path):
            # Write the file name and its hyperlink
            worksheet.cell(row=row, column=1).value = item
            worksheet.cell(row=row, column=1).hyperlink = f"file:///{item_path}"
            row += 1
        else:
            # Write the directory name as a title
            worksheet.cell(row=row, column=1).value = f"[{item}]"
            row += 1
            
            # Recursively write the hyperlinks of the subdirectories
            write_subdirectory_hyperlinks(item_path, worksheet, row)
            row += len(os.listdir(item_path)) + 1
    
    # Save the workbook
    workbook.save(excel_file_path)

def write_subdirectory_hyperlinks(subdirectory_path, worksheet, start_row):
    items = os.listdir(subdirectory_path)
    for i, item in enumerate(items):
        item_path = os.path.join(subdirectory_path, item)
        if os.path.isfile(item_path):
            worksheet.cell(row=start_row + i, column=1).value = item
            worksheet.cell(row=start_row + i, column=1).hyperlink = f"file:///{item_path}"

if __name__ == "__main__":
    directory_path = "c:/Users/Usuario/Desktop/Busquedas/CNS 2022 - Soldadura por Resistencia/15th Conf CANDU - 2022 presentaciones"
    excel_file_path = "./CANADA2022presentations.xlsx"
    write_hyperlinks_to_excel(directory_path, excel_file_path)

