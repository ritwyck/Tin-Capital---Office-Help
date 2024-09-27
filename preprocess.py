import os


def process_txt_file(txt_file, delimiter, lines_to_delete):
    try:
        with open(txt_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Remove the specified line to delete if present
        lines = [line for line in lines if line.strip() not in lines_to_delete]

        # Remove empty lines and lines that start with empty spaces
        lines = [line for line in lines if line.strip() !=
                 '' and not line.startswith(' ')]

        # Find the index of the delimiter line
        delimiter_index = next((i for i, line in enumerate(
            lines) if delimiter in line), len(lines))

        # Extract content before the delimiter
        extracted_content = lines[:delimiter_index]

        # Keep at most the first 5 lines
        if len(extracted_content) > 5:
            extracted_content = extracted_content[:5]

        # Overwrite the original file with the extracted content
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.writelines(extracted_content)

        print(f"Processed {txt_file}")

    except Exception as e:
        print(f"Failed to process {txt_file}: {e}")


def process_txts_in_folder(folder_path, delimiter, lines_to_delete):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                txt_file = os.path.join(root, file)
                process_txt_file(txt_file, delimiter, lines_to_delete)


# Replace 'folder_path' with the path to your folder containing .txt files
# Replace 'delimiter' with the line or keyword before which content should be retained
folder_path = '/Users/wiksrivastava/Desktop/tinCapital/Email_Confirmation/Emails'
delimiter = 'Van: _name_ | TIN Capital < name@tincapital.vc>'
lines_to_delete = [
   // lines deleted due to privacy concerns
]
process_txts_in_folder(folder_path, delimiter, lines_to_delete)
