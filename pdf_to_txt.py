# _*_ coding: UTF-8 _*_
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt

#converts pdf, returns its text content as a string
#from https://www.binpress.com/tutorial/manipulating-pdfs-with-python/167
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text 
   
#converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir
def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in 
    count=0
    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = pdfDir + pdf
            try:
                count+=1 
                if count % 5 ==0:
                    print("output: ",count,pdfFilename)

                text = convert(pdfFilename) #get string of text content of pdf
                textFilename = txtDir + pdf.split(".")[0] + ".txt"
                textFile = open(textFilename, "w",encoding="utf-8-sig") #make text file
                textFile.write(text) #write text to text file
            except Exception as e:
                print("error: ",count,pdfFilename,e)
                continue

#i : info
#p : pdfDir
#t = txtDir
def main(argv):
    pdfDir = ""
    txtDir = ""
    try:
        opts, args = getopt.getopt(argv,"ip:t:")
    except getopt.GetoptError:
        print("pdfToT.py -p <pdfdirectory> -t <textdirectory>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-i":
            print("pdfToT.py -p <pdfdirectory> -t <textdirectory>")
            sys.exit()
        elif opt == "-p":
            pdfDir = arg
        elif opt == "-t":
            txtDir = arg
    convertMultiple(pdfDir, txtDir)
    
if __name__ == "__main__":
    main(sys.argv[1:])
    
        

    
