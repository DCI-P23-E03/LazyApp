#pip install pdfquery

from pdfquery import PDFQuery

pdf = PDFQuery('Lebenslauf.pdf')
pdf.load()

# Use CSS-like selectors to locate the elements
text_elements = pdf.pq('LTTextLineHorizontal')

# Extract the text from the elements
text = [t.text for t in text_elements]

#print(text)
