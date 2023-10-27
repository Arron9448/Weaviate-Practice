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

# Ensure instance is live and ready
assert client.is_ready()

### Occupying WCS instance of weaviate with objects
## Erase data in Question class and its schema
#client.schema.delete_class("Question")

## Define data schema using text2vec-openai API
#class_obj = {
#    "class": "Question",
#    "vectorizer": "text2vec-openai",
#    "moduleConfig": {
#        "text2vec-openai": {},
#        "generative-openai": {}
#    }
#}

## Add Question schema
#client.schema.create_class(class_obj)

## Load 'Tiny Jeopardy!' sample data set
#resp = requests.get('https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json')
#data = json.loads(resp.text)

## Configure Weaviate batch, with
## - starting batch size of 100
#client.batch.configure(batch_size=100)

## Import data
#with client.batch as batch:
#    # Batch import all Questions
#    for i, d in enumerate(data):
#        print(f"importing question: {i+1}")
#        properties = {
#            "answer": d["Answer"],
#            "question": d["Question"],
#            "category": d["Category"],
#        }
#        batch.add_data_object(properties, "Question")

#print("Importing Questions complete")

### Sample Query - Semantic Search
#response = (
#    client.query
#    .get("Question", ["question", "answer", "category"])
#    .with_near_text({"concepts": ["biology"]})
#    .with_limit(2)
#    .do()
#)
#
# print(json.dumps(response, indent=4))

### Sample Query - Filtered Semantic Search
#response = (
#    client.query
#    .get("Question", ["question", "answer", "category"])
#    .with_near_text({"concepts": ["materials"]})
#    .with_where({
#        "path": ["category"],
#        "operator": "Equal",
#        "valueText": "SCIENCE"
#    })
#    .with_limit(2)
#    .do()
#)
#
#print(json.dumps(response, indent=4))

# Sample Query - RAG Search (Single Prompt)
response = (
    client.query
    .get("Question", ["question", "answer", "category"])
    .with_near_text({"concepts": ["materials"]})
    .with_generate(single_prompt="Explain {answer} as you might to a five-year-old.")
    .with_limit(2)
    .do()
)

print(json.dumps(response, indent=4))

