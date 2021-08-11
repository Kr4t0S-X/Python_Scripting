# importing required modules  
import PyPDF2
import os
from time import sleep

# ask the user to enter the path
search_path = input("Enter directory path to search: ")
file_type = input("File type: ")

#Append a directory separator if not already present
if not (search_path.endswith("/") or search_path.endswith("\\")):
    search_path = search_path + "/"

#if path does not exist, set it to current directory
if not os.path.exists(search_path):
    search_path = "."

# Repeat for each file in the directory
for fname in os.listdir(path=search_path):
    # Apply file type filter
    if fname.endswith(file_type):
        
        print(fname)
        
        #Open the .pdf files
        pdfFileObj = open(search_path + fname, 'rb')
        if pdfFileObj.isEncrypted:
            pdfFileObj.decrypt("")

        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        

        print(pdfReader.numPages) # will give total number of pages in pdf

        pageObj = pdfReader.getPage(0)
        pageObj

        sentences=(pageObj.extractText())
        sentences=sentences.split(",")

        search_keywords=['Cyber','Cyber Security','Cybersecurity ','Data','Data Security','Information Security','Data and Cyber Security Terms']

        for sentence in sentences:
            lst = []
            for word in search_keywords:
                if word in sentence:
                    lst.append(word)
            print('{0} key word(s) in sentence: {1} '.format(len(lst), ', '.join(lst)))
            print(sentence + "\n")
