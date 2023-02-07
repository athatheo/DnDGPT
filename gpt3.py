import os
import openai
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


def call_gpt(text):
  credential = DefaultAzureCredential()
  client = SecretClient(vault_url=f"https://gptsecrets.vault.azure.net", credential=credential)
  secret = client.get_secret('openai-auth')
  openai.api_key = secret
  response = openai.Completion.create(
    model="text-ada-001",
    prompt=text,
    max_tokens=20,
    temperature=0)
  return str(response['choices'][0]['text'])
