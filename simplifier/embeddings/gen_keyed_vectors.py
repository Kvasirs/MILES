import os
import sys
from gensim.models import KeyedVectors

if len(sys.argv) > 1:
    # Convert GloVe vectors to Word2Vec for gensim.
    print("Loading FastText vectors...")
    lang = sys.argv[1]
    fast_file = "cc." + lang + ".300.vec"
    model = KeyedVectors.load_word2vec_format(fast_file)
    # Load model as KeyVectors and then save.
    print("Saving vectors as KeyedVectors...")
    model.save(sys.argv[1] + ".kv")
    print("Done! Saved WEs for " + sys.argv[1] + " language.")
    print("Deleting vec file as no longer needed...")
    os.remove("cc." + lang + ".300.vec")
    print("Vec file deleted!")
else:
    print("Please enter the location of the GloVe word embeddings.")
    
