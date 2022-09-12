import pandas as pd 
import numpy as np
import nltk
nltk.download('punkt')

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize

def preprocess_data(paragraphs):
  text_join = ''.join(paragraphs)
  tokens = sent_tokenize(text_join)

  vectorizer = TfidfVectorizer()
  text_tfidf = vectorizer.fit_transform(tokens)
  return text_tfidf

def text_rank(text2vec, tokens):

  # calculate coisine similarity
  similarity_matrix = cosine_similarity(text2vec)
  for i in range(len(similarity_matrix)):
    similarity_matrix[i] = similarity_matrix[i] / np.sum(similarity_matrix[i])  # transforn into matrix G
    
  U = np.ones_like(similarity_matrix) / len(similarity_matrix) # add smooth
  factor = 0.15 
  A = (1 - factor) * similarity_matrix + factor * U

  limiting_dist = np.ones(len(A)) / len(A)
  threshold = 1e-8
  delta = float('inf')
  iters = 0

  while delta > threshold:
    iters += 1

    p = limiting_dist.dot(A)
    delta = np.abs(p - limiting_dist).sum()
    limiting_dist = p

  scores = limiting_dist
  sort_idx = np.argsort(-scores)
  return [tokens[i] for i in sort_idx[:20]]