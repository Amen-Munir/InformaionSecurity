from DESclass import DES

from PyPDF2 import PdfReader
from reportlab.pdfgen import canvas

def readStringfromPdf(filepath):
    try:
        reader = PdfReader(filepath)
        text = ""
        for page in reader.pages:
            text += page.extract_text() 
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""


def divideToChunksOf8(input_string):

    
    while len(input_string) % 8 != 0:
        input_string += "0"

 
    chunks = [input_string[i:i + 8] for i in range(0, len(input_string), 8)]
    return chunks

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def createPdf(content, output_file):
    try:
    
        doc = SimpleDocTemplate(output_file, pagesize=letter)
        styles = getSampleStyleSheet()
        style = styles['Normal']
        paragraph = Paragraph(content, style)
        doc.build([paragraph])
        print("PDF created successfully.")
    except Exception as e:
        print(f"Error creating PDF: {e}")




def funcMain():
    des = DES() 
    filepath= r""+ input("Enter the path of the pdf file: ")
    text= readStringfromPdf(filepath)
    # print("Text:", text)
    chunks = divideToChunksOf8(text)
    # print("Chunks:", chunks)
    encriptedStr=""
    listEncryoted=[]
    ch=input(f"Do you want to encrypt the file at {filepath} (y/n): ")
    if ch.lower() == "n":
        return
    else:
        for i in chunks:
            encriptedStr+= des.encryptionDES(i)
            listEncryoted.append(des.encryptionDES(i))

        createPdf(encriptedStr,"encrypted.pdf")

    ch=input(f"Do you want to decrypt the encrypted file just encrypted? (y/n): ")
    if ch.lower() == "n":
        return
    else:
        decrypted_text=""
        for i in listEncryoted:
            decrypted_text += des.decryptionDES(i)


        createPdf(decrypted_text,"decrypted.pdf")
        

funcMain()

