# Weaviate-Practice

Practice using Weaviates Python client to manage a WCS instance of Weaviate for 'Tiny Jeopardy!' data set.

Goals:
1. Build a Weaviate vector database
2. Query it with:
    - Semantic search
    - Added filters
    - generative searches to transform search results with a large language model (LLM).

Using:<br/>
- Sample datastore provided by Weaviate (https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json)
- text2vec-openai API to vectorize raw data

Proof of Success:<br/>
Semantic search for vectors most similar to 'biology' (nearText)<br/>
Query<br/>
    <img width="403" alt="image" src="https://github.com/Arron9448/Weaviate-Practice/assets/144850440/bb5e755f-d269-44bd-a6d1-cce5f8eec7b2"><br/>
Response<br/>
    <img width="1045" alt="image" src="https://github.com/Arron9448/Weaviate-Practice/assets/144850440/6a7a624b-2e97-4f71-b93a-4e91dcff9298"><br/>

Resources:<br/>
https://cookbook.openai.com/examples/vector_databases/weaviate/getting-started-with-weaviate-and-openai<br/>
https://weaviate.io/developers/wcs/quickstart<br/>
https://weaviate.io/developers/weaviate/quickstart<br/>
