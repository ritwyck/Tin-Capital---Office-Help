import pandas as pd

# Path to your CSV file
csv_file = '/Users/wiksrivastava/Desktop/tinCapital/file_classifications.csv'

# Read CSV file into pandas DataFrame
df = pd.read_csv(csv_file)

# Path to where you want to save the Excel file
excel_file = '/Users/wiksrivastava/Desktop/tinCapital/Email_Confirmationfile.xlsx'

# Write DataFrame to Excel file
df.to_excel(excel_file, index=False)

print(
    f'CSV file "{csv_file}" successfully converted to Excel file "{excel_file}"')
