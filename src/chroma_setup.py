import os
import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="knowledge_base"
)

for file in os.listdir("data"):

    if file.endswith(".txt"):

        path = os.path.join("data", file)

        with open(path, "r") as f:
            content = f.read()

        try:
            collection.add(
                documents=[content],
                ids=[file]
            )
        except:
            pass

print("Knowledge Base Loaded Successfully")
