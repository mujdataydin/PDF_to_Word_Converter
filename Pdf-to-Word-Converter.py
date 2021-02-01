print("Miklagard-S PDF to Word Converter")
print("Developed by Müjdat Aydın")

from pdf2docx import Converter
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory

Tk().withdraw()

pdf_file = askopenfilename(initialdir="/", title="Lütfen PDF dosyanızı seçin", filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")))
docx_file = "/Converted/" + input("Lütfen oluşturulacak Word dosyasının adını girin: ") + ".docx"

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()

print("Yeni Word dosyanızı C:" + docx_file + " adresinde bulabilirsiniz.")
