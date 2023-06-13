# Extract text from each of the raw PDFS
import PyPDF4
import os

dir = "tenth-edition/raw-pdfs"

for file in os.listdir(dir):
  if not file.endswith(".pdf"):
    continue
  with open("{}/{}".format(dir,file), 'rb') as pdfFileObj:
    pdfReader = PyPDF4.PdfFileReader(pdfFileObj)

    page_count = pdfReader.numPages
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    first_lines = text.split('\n')[1:5]

    print (f"File: {file}")
    print (f"Page Count: {page_count}")
    print (f"Text: {first_lines}")

    print("---------")

#file = "tenth-edition/raw-pdfs/76CPCqo7msJIHqzx.pdf"
