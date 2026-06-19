import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection("knowledge_base")

def retrieve_context(query):

    results = collection.query(
        query_texts=[query],
        n_results=1
    )

    if results["documents"] and len(results["documents"][0]) > 0:
        return results["documents"][0][0]

    return "No relevant information found."
