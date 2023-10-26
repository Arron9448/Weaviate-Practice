# Weaviate-Practice

Practice using Weaviates Python client to manage a WCS instance of Weaviate for 'Tiny Jeopardy!' data set.

**Goals:**
1. Build a Weaviate vector database
2. Query it with:
    - Semantic search
    - Added filters
    - generative searches to transform search results with a large language model (LLM)
<br/>

**Using:**<br/>
- Sample datastore provided by Weaviate (https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json)
- text2vec-openai API to vectorize raw data
<br/>

**Outcome:**<br/>
Objects added to target class.<br/>
<img width="1029" alt="image" src="https://github.com/Arron9448/Weaviate-Practice/assets/144850440/0633055b-26f5-42d4-b265-26bf4dab2963"><br/>
Semantic search for objects with vectors most similar to 'biology'.<br/>
![queryandresponse1](https://github.com/Arron9448/Weaviate-Practice/assets/144850440/69ba0b7d-e8d6-4ab5-865f-9134fe80c171)<br/>
Filtered semantic search for objects of 'SCIENCE' catagory most similar to 'materials'.<br/>
![queryandresponse2](https://github.com/Arron9448/Weaviate-Practice/assets/144850440/dc0a36c6-fd30-4efb-a2cb-85589441f47f)

<br/>

**Resources:**<br/>
https://cookbook.openai.com/examples/vector_databases/weaviate/getting-started-with-weaviate-and-openai<br/>
https://weaviate.io/developers/wcs/quickstart<br/>
https://weaviate.io/developers/weaviate/quickstart<br/>
