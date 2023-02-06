import os
import openai


def call_gpt(text):
  openai.api_key = os.environ['OPENAI_KEY']
  response = openai.Completion.create(
    model="text-ada-001",
    prompt=text,
    max_tokens=20,
    temperature=0)
  return str(response['choices'][0]['text'])
