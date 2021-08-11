#import packages
import PyPDF2
import re

#openpdf file
object = PyPDF2.PdfFileReader("gst-revenue-collection-march2020.pdf")

#get number of pages
NumPages = object.getNumPages()

#define keyterms
search_keywords=['GST','Ministry','%','Revenue','Year','Growth'] 

#extract text and do the search
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    print("This is page " + str(i))
    Text = PageObj.extractText()
    # print(Text)
    ResSearch = re.search(search_keywords, Text)
    print(ResSearch)
