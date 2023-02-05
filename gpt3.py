import os
import openai


def call_gpt():
  openai.api_key = os.getenv("OPENAI_KEY")
  return openai.Completion.create(
    model="text-ada-001",
    prompt="What is 5+5",
    max_tokens=20,
    temperature=0
  )