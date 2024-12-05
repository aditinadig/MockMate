from transformers import AutoTokenizer, AutoModel
import torch

# Load pre-trained Sentence-BERT model
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

def compute_similarity(question, response):
    """Compute semantic similarity between the question and response."""
    # Tokenize and encode question and response
    inputs = tokenizer([question, response], padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        embeddings = model(**inputs).pooler_output  # Pooler output as sentence embeddings

    # Compute cosine similarity
    question_embedding, response_embedding = embeddings[0], embeddings[1]
    similarity = torch.nn.functional.cosine_similarity(
        question_embedding, response_embedding, dim=0
    ).item()

    return similarity  # Ensure this is a float