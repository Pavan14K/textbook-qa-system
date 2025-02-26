import os
import streamlit as st
from transformers import pipeline
import pickle


st.title("Textbook QA System")

query = st.text_input("Enter your query:")
base_dir = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(base_dir, '..', 'data', 'index1.pkl')  # Update with your actual index file path

if query:
    with open(index_path, 'rb') as f:
        root = pickle.load(f)
    
    corpus = []
    for node in root.descendants:
        if hasattr(node, 'content'):
            corpus.append(node.content)
    
    context = " ".join(corpus)
    qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
    result = qa_pipeline(question=query, context=context)
    
    st.write("Answer:", result['answer'])
    st.write("Context:", result['context'])
    
def main():
    print("Index loaded successfully!")

if __name__ == '__main__':
    main()