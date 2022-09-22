from sentence_transformers import SentenceTransformer
import numpy as np

sentences = ["I ate dinner.",
             "We had a three-course meal.",
             "Brad came to dinner with us.",
             "He loves fish tacos.",
             "In the end, we all felt like we ate too much.",
             "We all agreed; it was a magnificent evening."]


def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))


model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

sentence_embeddings = model.encode(sentences)
query = "I had pizza and pasta"
query_vec = model.encode([query])[0]

for sent in sentences:
    sim = cosine(query_vec, model.encode([sent])[0])
    print("Sentence = ", sent, "; similarity = ", sim)



