from transformers import pipeline
import pickle

def generate_answer(query, index_path):
    with open(index_path, 'rb') as f:
        root = pickle.load(f)
    
    corpus = []
    for node in root.descendants:
        if hasattr(node, 'content'):
            corpus.append(node.content)
    
    qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
    context = " ".join(corpus)
    
    result = qa_pipeline(question=query, context=context)
    return result['answer']

if __name__ == "__main__":
    import sys
    query = sys.argv[1]
    index_path = sys.argv[2]
    
    answer = generate_answer(query, index_path)
    print(answer)
