from posix import listdir
import PyPDF2
import sys
import os

path = input('Enter directory to search for and merge pdfs: ') # Example: ~/so-many-pdfs"
pathname = str(path)
folder = os.listdir(path)
writer = PyPDF2.PdfFileWriter()

for file in folder:
    if file.endswith(".pdf"):
        file = pathname + "/" + file
        pdf = open(file, "rb")
        reader = PyPDF2.PdfFileReader(pdf)
    else:
        continue

    for pageNum in range(reader.numPages):
        page = reader.getPage(pageNum)
        writer.addPage(page)
    
pdf.close()

outputFile = open('../combinedfiles.pdf', 'wb')
writer.write(outputFile)
outputFile.close()