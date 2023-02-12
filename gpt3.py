import os
import openai
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


def call_gpt(text):
  credential = DefaultAzureCredential()
  client = SecretClient(vault_url=f"https://gptsecrets.vault.azure.net", credential=credential)
  secret = client.get_secret('openai-auth')
  openai.api_key = secret.value
  response = openai.Completion.create(
    model="text-ada-001",
    prompt="Create AC, HP, and speed for a D&D monster named: "+text,
    max_tokens=20,
    temperature=0)
  statblock = str(response['choices'][0]['text'])
  response = openai.Completion.create(
    model="text-ada-001",
    prompt="Create Ability Scores for a D&D monster named: "+text,
    max_tokens=20,
    temperature=0)
  statblock = statblock + " " + str(response['choices'][0]['text'])
  response = openai.Completion.create(
    model="text-ada-001",
    prompt="Create Skills, Senses, Languages and CR for a D&D monster named: "+text,
    max_tokens=20,
    temperature=0)
  statblock = statblock + " " + str(response['choices'][0]['text'])
  response = openai.Completion.create(
    model="text-ada-001",
    prompt="Create Actions for a D&D monster named: "+text,
    max_tokens=20,
    temperature=0)
  statblock = statblock + " " + str(response['choices'][0]['text'])
  return statblock
