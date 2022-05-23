import pandas as pd 
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
import time


def ngrams(string, n=3):

    string = re.sub(r'[,-./]|\sBD',r'', string)
    ngrams = zip(*[string[i:] for i in range(n)])
    return [''.join(ngram) for ngram in ngrams]

vectorizer = TfidfVectorizer(min_df=1, analyzer=ngrams)
df = pd.read_csv("names.txt")
names_auth = df['Titles']

tf_idf_matrix = vectorizer.fit_transform(names_auth)