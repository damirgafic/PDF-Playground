import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combine(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('combined.pdf')

pdf_combine(inputs)

#with open('dummy.pdf', 'rb') as file:
#    reader = PyPDF2.PdfFileReader(file)
#    page = reader.getPage(0)
#    page.rotateClockwise(180)
#    writer = PyPDF2.PdfFileWriter()
#    writer.addPage(page)
#    with open('tilt.pdf', 'wb') as new_file:
#        writer.write(new_file)
