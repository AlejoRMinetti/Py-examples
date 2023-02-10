import os
import openpyxl

def write_hyperlinks_to_excel(directory_path, excel_file_path):
    # Get all the files in the directory
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    
    # Create a workbook
    workbook = openpyxl.Workbook()
    
    # Get the active worksheet
    worksheet = workbook.active
    
    # Write the header
    worksheet['A1'] = "File Name"
    worksheet['B1'] = "Hyperlink"
    
    # Write the files and their hyperlinks
    for i, file in enumerate(files):
        row = i + 2
        worksheet.cell(row=row, column=1).value = file
        worksheet.cell(row=row, column=1).hyperlink = f"file:///{os.path.join(directory_path, file)}"
    
    # Save the workbook
    workbook.save(excel_file_path)


if __name__ == "__main__":
    directory_path = "./"
    excel_file_path = "./hiperlinks.xlsx"
    write_hyperlinks_to_excel(directory_path, excel_file_path)
