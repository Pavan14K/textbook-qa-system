# verify_installation.py
import torch
import torchvision
import transformers
from transformers import pipeline
import tf_keras as keras

print("Torch version:", torch.__version__)
print("Torchvision version:", torchvision.__version__)
print("Transformers version:", transformers.__version__)

# Verify pipeline function
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
print("Pipeline loaded successfully!")
