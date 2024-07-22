from transformers import pipeline

def generate_answer(query, context):
    qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
    result = qa_pipeline(question=query, context=context)
    return result['answer']

if __name__ == "__main__":
    import sys
    query = sys.argv[1]
    context = sys.argv[2]
    
    answer = generate_answer(query, context)
    print(answer)
