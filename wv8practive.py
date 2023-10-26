from dotenv import load_dotenv
load_dotenv() 

import weaviate
import os
import json

# Get API keys and WCS url (hidden as enviroment variables)
wcs_url = os.environ.get('My-Weaviate-Endpoint')
weaviate_key = os.environ.get('My-Weaviate-API-Key')
openai_key = os.environ.get('My-OpenAI-Api-Key')

client = weaviate.Client(
    url = wcs_url,
    auth_client_secret=weaviate.AuthApiKey(api_key=weaviate_key),
    additional_headers = {
        "X-OpenAI-Api-Key": openai_key
    }
)
