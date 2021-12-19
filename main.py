import openai
import gpdf
import tkinter as tk
from tkinter import simpledialog

####gui
ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
USER_INP = simpledialog.askstring(title="Test",
                                  prompt="What's your Name?:")

# check it out
print("Hello", USER_INP)


#summary

gpdf.getPaper(r'https://arxiv.org/pdf/2112.08990.pdf', filename="random_paper.pdf")

#asign file name
paperFilePath ="random_paper.pdf"
#extract content with pdf pdfplumber
paperContent = gpdf.getPaperContent(paperFilePath)

paperSummary = gpdf.getPaperSummary(paperContent)

print('...')
print('...')
print('...')
print()
print(paperSummary)