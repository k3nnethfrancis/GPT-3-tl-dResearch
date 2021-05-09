#! python3

#libraries
import openai
import os
from gpt import GPT
from gpt import Example

#get api ket
my_secret = os.environ['API_KEY']
openai.api_key = my_secret

#init gpt engine
gpt = GPT(engine="curie",
          temperature=0.5,
          max_tokens=75)

#load abstract
#with open('abstract.txt', 'r') as file:
#    abstract = file.read().replace('\n', '')

#gpt.add_example(Example("what are the key points from this text:", abstract))

#load paper
with open('fullpaper.txt', 'r') as file:
    paper = file.read().replace('\n', '')

gpt.add_example(Example("what are the key points from this text:", paper))


prompt = "what are the key points from this text?"

output = gpt.submit_request(prompt)

output.choices[0].text

print(gpt.get_top_reply(prompt))



