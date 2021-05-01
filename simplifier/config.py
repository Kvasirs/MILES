import torch

# Current language for simplification.
lang = "en"

# If word embeddings have been loaded.
loaded_embeddings = False

# Threshold for finding complex words from frequency.
min_complexity = 4.5

# Number of candidates to generate.
candidate_num = 10

# Use cuda if GPU is detected, otherwise use CPU.
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# List of supported languages.
supported_langs = ["ar","bg","ca","cs","da",
                   "nl","en","fi","fr","de",
                   "id","it","nb","pl","pt","ro",
                   "ru","es","sv","tr","uk","hu"]
