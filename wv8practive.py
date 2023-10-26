import weaviate
import os
import json

# Load .env file
from dotenv import load_dotenv
load_dotenv() 

# Get API keys and WCS url (hidden as enviroment variables)
wcs_url = os.getenv("WEAVIATE_ENDPOINT")
weaviate_key = os.getenv("WEAVIATE_API_KEY")
openai_key = os.getenv("OPENAI_API_KEY")

# Connect to WCS instance of Weaviate
auth_config = weaviate.AuthApiKey(api_key=weaviate_key)
client = weaviate.Client(
    url = wcs_url,
    auth_client_secret=auth_config
)
client = weaviate.Client(
    url = wcs_url,
    auth_client_secret=weaviate.AuthApiKey(api_key=weaviate_key),
    additional_headers = {
        "X-OpenAI-Api-Key": openai_key
    }
)

# Define data collection
class_obj = {
    "class": "Question",
    "vectorizer": "text2vec-openai",
    "moduleConfig": {
        "text2vec-openai": {},
        "generative-openai": {}
    }
}

client.schema.create_class(class_obj)
