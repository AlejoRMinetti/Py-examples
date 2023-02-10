import os
import sys
import xlsxwriter

def write_to_excel(dir_path, excel_file):
    workbook = xlsxwriter.Workbook(excel_file)
    worksheet = workbook.add_worksheet()

    row = 0
    for root, dirs, files in os.walk(dir_path):
        if row > 0:
            worksheet.write(row, 0, '')
            row += 1

        worksheet.write(row, 0, root, workbook.add_format({'bold': True}))
        row += 1

        for file in files:
            file_path = os.path.join(root, file)
            worksheet.write_url(row, 0, file_path, string=file)
            row += 1

    workbook.close()

if __name__ == '__main__':
    dir_path = sys.argv[1]
    excel_file = sys.argv[2] + ".xlsx"

    write_to_excel(dir_path, excel_file)
