#pip install pdfquery

from pdfquery import PDFQuery

pdf = PDFQuery('/home/user/Documents/DCI_CODE/LAZY/PDF input/indexmiete.pdf')
pdf.load()

# Use CSS-like selectors to locate the elements
text_elements = pdf.pq('LTTextLineHorizontal')

# Extract the text from the elements
text = [t.text for t in text_elements]

print(text)
