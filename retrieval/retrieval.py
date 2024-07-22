from rank_bm25 import BM25Okapi
import pickle

def retrieve_content(query, index_path):
    with open(index_path, 'rb') as f:
        root = pickle.load(f)
    
    corpus = []
    for node in root.descendants:
        if hasattr(node, 'content'):
            corpus.append(node.content)
    
    tokenized_corpus = [doc.split(" ") for doc in corpus]
    bm25 = BM25Okapi(tokenized_corpus)
    
    tokenized_query = query.split(" ")
    results = bm25.get_top_n(tokenized_query, corpus, n=5)
    return results

if __name__ == "__main__":
    import sys
    query = sys.argv[1]
    index_path = sys.argv[2]
    
    results = retrieve_content(query, index_path)
    for result in results:
        print(result)
