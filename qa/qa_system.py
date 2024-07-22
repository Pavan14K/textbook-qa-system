from transformers import pipeline
import pickle

def qa_pipeline(query, context):
    qa = pipeline("question-answering", model="deepset/roberta-base-squad2")
    result = qa(question=query, context=context)
    return result['answer']

if __name__ == "__main__":
    import sys
    query = sys.argv[1]
    context_path = sys.argv[2]
    
    with open(context_path, 'r') as f:
        context = f.read()
    
    answer = qa_pipeline(query, context)
    print(answer)
