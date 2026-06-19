import os

def retrieve_context(query):
    data_folder = "data"

    if not os.path.exists(data_folder):
        return "Knowledge base folder not found."

    query_words = query.lower().split()

    for file in os.listdir(data_folder):

        path = os.path.join(data_folder, file)

        if not os.path.isfile(path):
            continue

        # PDF files skip
        if file.endswith(".pdf"):
            continue

        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:

                content = f.read()

                if any(
                    word in content.lower()
                    for word in query_words
                ):
                    return content

        except Exception:
            continue

    return "No relevant information found."