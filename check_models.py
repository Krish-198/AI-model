from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()

client = OpenAI()

# List available models
models = client.models.list()

print("\nAvailable Models:\n")

for model in models.data:
    print(model.id)