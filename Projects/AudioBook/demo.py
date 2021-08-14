#pyPdf
#python to text speech(pytts)

import pyttsx3
import PyPDF2
import pdfplumber

file='mind-hacking ( PDFDrive ).pdf'

book=open(file,'rb')

#Create a pdf file reader
pdf_reader=PyPDF2.PdfFileReader(book)
pages=pdf_reader.numPages

#Create a pdfplumber object and loop through the number of pages in pdf file
with pdfplumber.open(file) as pdf:
    
    #Loops for iterating to go through every page
    for i in range(0,pages):
        page=pdf.pages[i]
        text=page.extract_text()
        print(text)
        speaker=pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()