import os
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Directory containing the text files
directory = '/Users/wiksrivastava/Desktop/tinCapital/Email_Confirmation/Emails'

# List to store the contents of the files
file_contents = []

# Initialize TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Example function to classify text (modify this function based on your needs)


def classify_text(content):
    # Check if "Akkoord" or "akkoord" is in the content
    if "neit akkoord" in content or "Neit akkoord" in content or "Neit accoord" in content or "neit accoord" in content or "Geen akkoord" in content or "geen accoord" in content or "Geen accoord" in content or "geen accoord" in content or "nee akkoord" in content or "Nee akkoord" in content or "Nee accoord" in content or "nee accoord" in content or "akkoord neit" in content or "Akkoord neit" in content or "Accoord neit" in content or "accoord neit" in content or "akkoord geen" in content or "Akkoord  geen" in content or "Accoord geen" in content or "accoord geen" in content or "akkoord nee" in content or "Akkoord nee" in content or "accoord nee" in content or "Accoord nee" in content:
        return "rejected"
    if "Akkoord" in content or "akkoord" in content or "accoord" in content or "Accoord" in content:
        return "accepted"
    else:
        return "rejected"

# Function to extract desired part of the filename


def extract_part_of_filename(filename):
    avoid_patterns = [
       // removed due to privacy concerns    ]
    for avoid_before, avoid_after in avoid_patterns:
        start_index = filename.find(avoid_before) + len(avoid_before)
        end_index = filename.rfind(avoid_after)
        if start_index >= 0 and end_index >= 0 and start_index < end_index:
            return filename[start_index:end_index]
    return filename


# Loop through all files in the directory
for filename in os.listdir(directory):
    # Construct the full file path
    file_path = os.path.join(directory, filename)

    # Check if it is a file and ends with .txt extension
    if os.path.isfile(file_path) and filename.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:  # Specify encoding if necessary
            # Read the content of the file
            content = file.read()
            # Extract desired part of filename, avoiding specific patterns
            file_name = extract_part_of_filename(filename)

            # Classify the text
            classification = classify_text(content)

            # Append the information to the list as a dictionary
            file_contents.append({
                'file_name': file_name,
                'file_text': content,
                'text_classification': classification
            })

# Write to CSV file
csv_filename = 'file_classifications.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['File Name', 'File Text', 'File Classification']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for entry in file_contents:
        writer.writerow({
            'File Name': entry['file_name'],
            'File Text': entry['file_text'],
            'File Classification': entry['text_classification']
        })

print(f"CSV file '{csv_filename}' saved successfully.")
