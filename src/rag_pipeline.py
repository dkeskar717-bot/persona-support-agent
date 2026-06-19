import os

def retrieve_context(query):
    data_folder = "data"

    for file in os.listdir(data_folder):
        path = os.path.join(data_folder, file)

        with open(path, "r") as f:
            content = f.read()

            if any(word.lower() in content.lower() for word in query.split()):
                return content

    return "No relevant information found."
