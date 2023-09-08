# pip install pdfplumber

import pdfplumber

pdf_file_path = (
    "/home/user/Documents/DCI_CODE/LAZY/PDF input/20003 ME Index 01.08.2023.pdf"
)

with pdfplumber.open(pdf_file_path) as pdf:
    pdf_content = ""
    for page in pdf.pages:
        pdf_content += page.extract_text()

print(pdf_content)
