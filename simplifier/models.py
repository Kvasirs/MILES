from transformers import BertForMaskedLM, BertTokenizer, logging
from gensim.models import KeyedVectors
from nltk.stem import PorterStemmer

import nltk
import torch
import math

from . import config

# Word embeddings.
embeddings = None

# Surpress warnings.
logging.set_verbosity(logging.ERROR)

# Load BERT model and tokenizer.
tokenizer = BertTokenizer.from_pretrained("bert-base-multilingual-uncased")
model = BertForMaskedLM.from_pretrained("bert-base-multilingual-uncased")

# Create stemmer object.
stemmer = PorterStemmer()

def load_embeddings(language):
    """Load word embeddings for selected language."""
    try:
        wv_path = "simplifier/embeddings/" + config.lang + ".kv"
        wv_model = KeyedVectors.load(wv_path, mmap='r')
        print("Loaded embeddings!")
    except FileNotFoundError:
        print("No embeddings for " + config.lang + " found. Using without...")
        wv_model = None
    return wv_model
