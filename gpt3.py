import os
import openai
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


def call_gpt(text):
  model_name = "text-davinci-003"
  credential = DefaultAzureCredential()
  client = SecretClient(vault_url=f"https://gptsecrets.vault.azure.net", credential=credential)
  secret = client.get_secret('openai-auth')
  openai.api_key = secret.value
  response = openai.Completion.create(
    model=model_name,
    prompt="Create AC, HP, and speed for a D&D monster named: "+text,
    max_tokens=20,
    temperature=0)
  statblock = str(response['choices'][0]['text'])
  response = openai.Completion.create(
    model=model_name,
    prompt="Create Ability Scores for a D&D monster named: "+text,
    max_tokens=60,
    temperature=0)
  statblock = statblock + "\n " + str(response['choices'][0]['text'])
  response = openai.Completion.create(
    model=model_name,
    prompt="Create Skills, Senses, Languages and CR for a D&D monster named: "+text,
    max_tokens=200,
    temperature=0)
  statblock = statblock + "\n " + str(response['choices'][0]['text'])
  response = openai.Completion.create(
    model=model_name,
    prompt="Create Actions for a D&D monster named: "+text,
    max_tokens=200,
    temperature=0)
  statblock = statblock + "\n " + str(response['choices'][0]['text'])
  return statblock

## I can sanitize strings and reask if the the response doesnt have what i asked
## Then i have to put it in specific 
