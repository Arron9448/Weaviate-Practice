import weaviate
import os
import requests
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
    auth_client_secret=weaviate.AuthApiKey(api_key=weaviate_key),
    additional_headers = {
        "X-OpenAI-Api-Key": openai_key
    }
)

# Define data collection using OpenAI Vectorizer
class_obj = {
    "class": "Question",
    "vectorizer": "text2vec-openai",
    "moduleConfig": {
        "text2vec-openai": {},
        "generative-openai": {}
    }
}

#client.schema.create_class(class_obj)

# Batch import/vectorize sample data
resp = requests.get('https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json')
data = json.loads(resp.text) # Load data
client.batch.configure(batch_size=100) # Configure batch
with client.batch as batch:
    for i, d in enumerate(data):
        print(f"importing question: {i+1}")
        properties = {
            "answer": d["Answer"],
            "question": d["Question"],
            "category": d["Category"],
        }
        batch.add_data_object(
            data_object=properties,
            class_name="Question"
        )
