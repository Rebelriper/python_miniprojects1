import pdfplumber
import fitz
from pypdf import PdfReader
reader=PdfReader('C prg goto _storage_classes.pdf')
#print(len(reader.pages))
page=reader.pages[0]
for i in range(len(reader.pages)):
    page=reader.pages[i]
    print(page.extract_text())

for i in page.images:
    with open(i.name,'wb') as f:
        f.write(i.data)

with pdfplumber.open('C prg goto _storage_classes.pdf') as f:
    for i in f.pages:
        print(i.extract_tables())

doc =fitz.open('C prg goto _storage_classes.pdf')
print(doc.page_count)
print(doc.metadata)
links=page.get_links()
print(links)
