import weaviate
import os
import json

from dotenv import load_dotenv
load_dotenv() 

# Get API keys and WCS url (hidden as enviroment variables)
wcs_url = os.getenv("WEAVIATE_ENDPOINT")
weaviate_key = os.getenv("WEAVIATE_API_KEY")
openai_key = os.getenv("OPENAI_API_KEY")

# Connect to WCS instance of Weaviate
client = weaviate.Client(
    url = wcs_url,
    auth_client_secret=weaviate.AuthApiKey(api_key=weaviate_key),
    additional_headers = {
        "X-OpenAI-Api-Key": openai_key
    }
)

