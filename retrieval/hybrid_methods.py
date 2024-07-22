from transformers import pipeline
from rank_bm25 import BM25Okapi
import pickle

def hybrid_retrieve(query, index_path):
    with open(index_path, 'rb') as f:
        root = pickle.load(f)
    
    corpus = []
    for node in root.descendants:
        if hasattr(node, 'content'):
            corpus.append(node.content)
    
    tokenized_corpus = [doc.split(" ") for doc in corpus]
    bm25 = BM25Okapi(tokenized_corpus)
    
    tokenized_query = query.split(" ")
    bm25_results = bm25.get_top_n(tokenized_query, corpus, n=5)
    
    dpr = pipeline("feature-extraction", model="facebook/dpr-ctx_encoder-single-nq-base")
    query_embedding = dpr(query)[0]
    dpr_scores = [dpr(doc)[0] for doc in bm25_results]
    
    combined_scores = [(bm25_score + dpr_score) for bm25_score, dpr_score in zip(bm25_results, dpr_scores)]
    sorted_results = sorted(zip(bm25_results, combined_scores), key=lambda x: x[1], reverse=True)
    
    return [result[0] for result in sorted_results]

if __name__ == "__main__":
    import sys
    query = sys.argv[1]
    index_path = sys.argv[2]
    
    results = hybrid_retrieve(query, index_path)
    for result in results:
        print(result)
