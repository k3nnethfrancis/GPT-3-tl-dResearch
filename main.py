#! python3

#libraries
import os
import openai
import wget
import pathlib
import pdfplumber

#write a function that downloads a pdf from an arxiv address
def getPaper(paper_url, filename="random_paper.pdf"):
  """
  Downloads a paper from it's arxiv page and returns
  the local path to that file.
  """
  downloadedPaper = wget.download(paper_url, filename)    
  downloadedPaperFilePath = pathlib.Path(downloadedPaper)

  return downloadedPaperFilePath

#asign file name

paperFilePath ="ona.pdf"
paperURL = r'https://arxiv.org/pdf/2112.08990.pdf'

#download paper
#getPaper(paperURL, paperFilePath)

#extract content with pdf pdfplumber
def getPaperContent(paperFilePath):
  return pdfplumber.open(paperFilePath).pages

paperContent = getPaperContent(paperFilePath)
#func to display content
def displayPaperContent(paperContent, page_start=0, page_end=5):
    for page in paperContent[page_start:page_end]:
        print(page.extract_text())
#run func
displayPaperContent(paperContent)

#open ai API
my_secret = os.environ['API_KEY']

#summarize paper
def getPaperSummary(paperContent):
    tldr_tag = "\n tl;dr:" #writing the tag so that the GPT-3 model knows when the text stops and when it should start the completion
    openai.api_key = my_secret
    #engine_list = openai.Engine.list()
    
    for page in paperContent:    
        text = page.extract_text() + tldr_tag #xtracting the text from each page and feeding it to the model
        response = openai.Completion.create(engine="davinci",prompt=text,temperature=0.3,
            max_tokens=140,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"]
        )
        summary = response["choices"][0]["text"]

    return summary

paperSummary = getPaperSummary(paperContent)

print('...')
print('...')
print('...')
print()
print('Summary:',paperSummary)