import os
import tkinter
from tkinter import filedialog
from PyPDF2 import PdfFileReader, PdfFileWriter

import sys

import webbrowser


def encrypt_pdf(filename):
    print(filename)
    pdf_reader = PdfFileReader(filename)
    pdf_writer = PdfFileWriter()
    password = input("Write a password!\n")

    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))
    pdf_writer.encrypt(user_pwd=password, use_128bit=True)
    with open(filename + ".encrypted.pdf", "wb") as out:
        pdf_writer.write(out)
    print("Successful encrypted")


def merge_pdfs(result_name):
    pdf_writer = PdfFileWriter()
    root = tkinter.Tk()
    files = filedialog.askopenfilenames(parent=root,
                                        title="Pick PDFs!")
    for file in root.tk.splitlist(files):
        pdf_reader = PdfFileReader(file)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    print('PDFs merged.')
    path = os.path.join('C:/Users/' + os.getlogin() + '/' + sys.argv[2] + '/', result_name)
    if not os.path.exists(path):
        with open(path, 'wb') as out:
            pdf_writer.write(out)
            print("PDF successful created!.")
        answerEncyrpt = input("Do you want encrypt this PDF file? (y/n): ")

        if answerEncyrpt == 'y':
            encrypt_pdf(path)
        webbrowser.open_new(path)
    else:
        print("File already exist")


def merge_or_encrypt(answer):
    if answer == "m":
        merge_pdfs(sys.argv[1])
    elif answer == "e":
        filename = filedialog.askopenfile().name
        encrypt_pdf(filename)


answer_merge_or_encrypt = input("Mergen or encrypten? (m/e): ")
merge_or_encrypt(answer_merge_or_encrypt)
