import openpyxl

def copy_cells(source_file, source_sheet_name, source_range, output_file="", output_sheet_name="hoja1", output_cell="A2"):
    """
    Copy a range of cells from the source Excel file to the output Excel file.
    """
    source_wb = openpyxl.load_workbook(source_file)
    source_ws = source_wb[source_sheet_name]

    # Extract the source values from the range and store in a list of lists
    source_values = []
    for row in source_ws[source_range]:
        source_values.append([cell.value for cell in row])

    # Create the output workbook and sheet
    if output_cell == "":
        #create new file
        output_wb = openpyxl.Workbook()
    else:
        #using templates
        output_wb = openpyxl.load_workbook(output_file)
    output_ws = output_wb[output_sheet_name]

    # Loop through the source values and paste them into the output sheet
    for row_idx, row in enumerate(source_values):
        for col_idx, value in enumerate(row):
            output_ws[output_cell].offset(row=row_idx, column=col_idx).value = value

    # Save the output workbook
    output_wb.save(output_file)

if __name__ == '__main__':
    copy_cells("./demosheet.xlsx", "Sheet", "A2:C4", "templateSample.xlsx","Hoja1", "A2")