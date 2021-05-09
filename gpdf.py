#! python3

#packages
import openai
import wget
import pathlib

#function to download a pdf of the paper
def getPaper(paper_url, filename=""):
    """
    Downloads a paper from it's arxiv page and returns
    the local path to that file.
    """
    downloadedPaper = wget.download(paper_url, filename)    
    downloadedPaperFilePath = pathlib.Path(downloadedPaper)

    return downloadedPaperFilePath

#function to convert paper to text
def displayPaperContent(paperContent, page_start=0, page_end=5):
    for page in paperContent[page_start:page_end]:
        print(page.extract_text())

#feed gpt3 paper text
def showPaperSummary(paperContent):
    #setting the tag so gpt3 knows when the text stops and when to start the completion
    tldr_tag = "\n\n tl;dr:" 
    #set up environment
    openai.organization = 'org-cur38Rg6pd6JFV2pDFNAFtEh'
    openai.api_key = "sk-JXm3aEq3AAUezUoKjGD2qCJ46xf5aAEUmMmUsbwf"
    # calling the engines available from the openai api 
    engine_list = openai.Engine.list()

    #extract the text from each page
    for page in paperContent:    
        text = page.extract_text() + tldr_tag
        #feeding the text to the model
        response = openai.Completion.create(engine="curie",prompt=text,temperature=0.3,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"]
        )
        print(response["choices"][0]["text"])