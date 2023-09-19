import csv
import openpyxl
import os

# Directory containing CSV files
csv_directory = 'csv_files/'

# Output directory for XLSX files
xlsx_directory = 'xlsx_files/'

# Ensure the output directory exists
os.makedirs(xlsx_directory, exist_ok=True)


def csv_to_excel(csv_filename, excel_filename):
    # Read CSV file
    csv_data = []
    with open(csv_filename) as f:
        csv_data = [row for row in csv.reader(f)]

    # Write to Excel file
    workbook = openpyxl.workbook.Workbook()
    worksheet = workbook.active
    for row in csv_data:
        worksheet.append(row)
    workbook.save(excel_filename)


# Convert all CSV files in the directory to XLSX files
for filename in os.listdir(csv_directory):
    csv_to_excel(csv_directory + filename, xlsx_directory + filename.replace('.csv', '.xlsx'))
