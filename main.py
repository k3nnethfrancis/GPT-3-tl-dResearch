#!python
import time
import gpdf

#define opening sequence
def init():
  print('Hello...')
  time.sleep(1.5)
  print('')
  url = input('Enter the url to summarize: ')
  return url

if __name__ == "__main__":
  # url = init()
  # # https://arxiv.org/pdf/2112.08990.pdf
  # fmt_url = str(url)
  # gpdf.getPaper(fmt_url, filename="random_paper.pdf")

  #asign file name
  paperFilePath ="hrmj3.pdf"
  #extract content with pdf pdfplumber
  paperContent = gpdf.getPaperContent(paperFilePath)

  paperSummary = gpdf.getPaperSummary(paperContent)

  print('...')
  print('...')
  print('...')
  print()
  print(paperSummary)