#! python3

#libraries
from gpdf import showPaperSummary
import pdfplumber
import os

#show the summary
#convert pdf to text
paperFilePath = "hrmj3.pdf"
paperContent = pdfplumber.open(paperFilePath).pages
showPaperSummary(paperContent)



