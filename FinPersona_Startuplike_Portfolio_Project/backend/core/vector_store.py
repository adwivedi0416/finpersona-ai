def search(document,query):
    chunks=[x.strip() for x in document.split('.') if x.strip()]
    return chunks[:4]
