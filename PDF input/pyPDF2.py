#pip install PyPDF2

import PyPDF2

# Open the PDF file in binary read mode
pdf_file_path = '/home/user/Documents/DCI_CODE/LAZY/PDF input/Lebenslauf Simakov.pdf'
pdf_file = open(pdf_file_path, 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Initialize an empty string to store the content
pdf_content = ""

# Loop through each page and extract text
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    pdf_content += page.extract_text()

# Close the PDF file
pdf_file.close()

# Print or do something with the extracted content
print(pdf_content)
