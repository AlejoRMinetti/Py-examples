import argparse
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
    
    row = 2
    for item in items:
        item_path = os.path.join(directory_path, item)
        if os.path.isfile(item_path):
            # Write the file name and its hyperlink
            worksheet.cell(row=row, column=1).value = item
            worksheet.cell(row=row, column=1).hyperlink = f"file:///{item_path}"
            worksheet.cell(row=row, column=1).style = "Hyperlink"
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
            worksheet.cell(row=start_row + i, column=1).style = "Hyperlink"

if __name__ == "__main__":
    # Parse the command-line arguments
    parser = argparse.ArgumentParser(description="Write the hyperlinks of the files and subdirectories in a directory to an Excel file.")
    parser.add_argument("directory_path", help="The path of the directory to be processed.")
    parser.add_argument("excel_file_path", help="The path of the Excel file to be created.")
    args = parser.parse_args()
    
    write_hyperlinks_to_excel(args.directory_path, args.excel_file_path)


# to use:
# py hyperlinkCLapp.py ./ ./file.xlsx

