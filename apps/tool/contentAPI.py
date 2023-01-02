import os
import openai
from apps import config
openai.api_key = config.Config.OPENAI_API_KEY

#text-ada-001,text-babbage-001,text-babbage-001,text-davinci-002
def OpenAPI(query,spTool):
  if spTool['stop']:
      response = openai.Completion.create(
        model="text-davinci-002",
        prompt=query,
        temperature=int(spTool['temperature']),
        max_tokens=int(spTool['max_tokens']),
        top_p=int(spTool['top_p']),
        frequency_penalty=int(spTool['frequency_penalty']),
        presence_penalty=int(spTool['presence_penalty']),
        best_of=int(spTool['best_of']),
        stop=spTool['stop']
      )
  else:
       response = openai.Completion.create(
        model=spTool['model'],
        prompt=query,
        temperature=int(spTool['temperature']),
        max_tokens=int(spTool['max_tokens']),
        top_p=int(spTool['top_p']),
        frequency_penalty=int(spTool['frequency_penalty']),
        presence_penalty=int(spTool['presence_penalty']),
       )
  if 'choices' in response:
    if len(response['choices'])>0:
      answer,total_tokens = response['usage']['total_tokens'],response['choices'][0]['text']
    else:
      answer ='opps sorry, you best the AI this time'
  else:
      answer ='opps sorry, you best the AI this time'
  return answer,total_tokens
# query = 'Generate a blog ideas about car'
# worknig = {'model':"text-davinci-002",
#                 'best_of':1,
#                 'temperature':1,
#                 'max_tokens':4000,
#                 'top_p':1,
#                 'frequency_penalty':0.5,
#                 'stop':[],
#                 'presence_penalty':0 }

# print(OpenAPI(query,worknig))