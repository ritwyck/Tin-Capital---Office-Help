import pandas as pd


def xls_to_csv(xls_file_path, csv_file_path):
    # Read the Excel file
    excel_data = pd.read_excel(xls_file_path, sheet_name=None)

    # If the Excel file contains multiple sheets, convert each to a CSV file
    for sheet_name, data in excel_data.items():
        # Construct the CSV file name for each sheet
        sheet_csv_file_path = csv_file_path.replace(
            '.csv', f'_{sheet_name}.csv')
        # Write the data to a CSV file
        data.to_csv(sheet_csv_file_path, index=False)


# Example usage
xls_file_path = '/Users/wiksrivastava/Desktop/tinCapital/Email_Confirmation/Approval Financial Statement 2023 by investors.xlsx'
csv_file_path = '/Users/wiksrivastava/Desktop/tinCapital/Email_Confirmation/emailCSV.csv'
xls_to_csv(xls_file_path, csv_file_path)
