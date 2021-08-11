from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import os

user_input = input("Enter the path of the files to review: ")
files = os.listdir(user_input)

for file in files:
    print (file)
    pdfReader = PdfFileReader(open(files, 'rb'))
