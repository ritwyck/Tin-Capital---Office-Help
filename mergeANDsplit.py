import PyPDF2
import io

# Open the documents
document1_path = '/Users/wiksrivastava/Desktop/tinCapital/pdfEditor/input/document/rc.pdf'
document2_path = '/Users/wiksrivastava/Desktop/tinCapital/pdfEditor/input/signature/rc.pdf'
output_path = '/Users/wiksrivastava/Desktop/tinCapital/pdfEditor/output/rcInvestments.pdf'

document1 = open(document1_path, 'rb')
document2 = open(document2_path, 'rb')

# Create PDF reader objects
pdf_reader1 = PyPDF2.PdfReader(document1)
pdf_reader2 = PyPDF2.PdfReader(document2)

# Create a PDF writer object
pdf_writer = PyPDF2.PdfWriter()

# Page number to replace (zero-based index)
page_to_replace = 10  # For example, replace the third page

# Add pages from document 1 to the writer, replacing the specified page
for i in range(len(pdf_reader1.pages)):
    if i == page_to_replace:
        # Add the page from document 2
        pdf_writer.add_page(pdf_reader2.pages[0])
    else:
        # Add the page from document 1
        pdf_writer.add_page(pdf_reader1.pages[i])

# Write the modified content to a new PDF
with open(output_path, 'wb') as output_file:
    pdf_writer.write(output_file)

# Close the files
document1.close()
document2.close()
