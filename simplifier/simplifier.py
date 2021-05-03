from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.tokenize import wordpunct_tokenize as tokenize

from wordfreq import zipf_frequency as zfreq
from stop_words import safe_get_stop_words
from gensim.models import KeyedVectors

from .features import *
from .models import *
from . import config

def generate_candidates(tokens, index, topn=config.candidate_num):
    """Generates candidates for word using BERT model."""
    # Create sentence pair to pass to BERT from tokens.
    sentence = " ".join(tokens)
    masked_sentence = sentence.replace(tokens[index], "[MASK]")
    bert_sentence = f'[CLS] {sentence} [SEP] {masked_sentence} [SEP] '
    bert_tokens = tokenizer.tokenize(bert_sentence)
    
    # Get masked token index, index for all tokens in vocab, and segment ids.
    masked_index = [i for i, x in enumerate(bert_tokens) if x == '[MASK]'][0]
    indexed_tokens = tokenizer.convert_tokens_to_ids(bert_tokens)
    segments_ids = [0] * len(bert_tokens)

    # Convert tokens into tensors.
    tokens_tensor = torch.tensor([indexed_tokens])
    segments_tensors = torch.tensor([segments_ids])

    # Put everything on cuda.
    tokens_tensor = tokens_tensor.to(config.device)
    segments_tensors = segments_tensors.to(config.device)
    model.to(config.device)

    # Predict all tokens.
    with torch.no_grad():
        outputs = model(tokens_tensor, token_type_ids=segments_tensors)
        predictions = outputs[0][0][masked_index]

    # Get predictions and return ordered.
    predicted_ids = torch.argsort(predictions, descending=True)[:config.candidate_num]
    predicted_tokens = tokenizer.convert_ids_to_tokens(list(predicted_ids))

    return predicted_tokens

def suitable_complex_word(w):
    """Checks if detected word is suitable for replacing."""
    # Not stopword or punctuation.
    not_stopword = w not in safe_get_stop_words(config.lang) and w.isalpha()
    # Not a simple word (above defined threshold).
    not_simple = zfreq(w, config.lang) < config.min_complexity
    # No uppercase (ensures NEs are not simplified).
    not_uppercase = w.islower()

    return not_stopword and not_simple and not_uppercase

def suitable_candidate(w, c):
    """Checks if candidate is a suitable substitute based on
    various criteria."""
    source_stem = stemmer.stem(w)
    candidate_stem = stemmer.stem(c)

    # Check stem length.
    not_stem_len = not(len(candidate_stem) >= 3 and candidate_stem[:3] == source_stem[:3])
    # Not sharing stem with original word.
    not_equal_stem = source_stem != candidate_stem
    # Not punctuation
    not_punctuation = c.isalpha()

    # Other checks (disable when benchmarking).
    not_morph_deriv = c not in w and w not in c
    not_complex = zfreq(c, config.lang) > zfreq(w, config.lang)
    not_stopword = c not in safe_get_stop_words(config.lang) and c.isalpha()

    return not_equal_stem and not_stem_len and not_morph_deriv and not_stopword and not_complex
    
def simplify_token(tokens, i):
    """Simplifies a token given index and all tokens."""
    # Generate candidates using BERT.
    candidates = generate_candidates(tokens, i)

    # Start ranking candidates on different features.
    candidates = [c for c in candidates if suitable_candidate(tokens[i], c)][::-1]
    complex_ranked = sorted(candidates, key = lambda c: zfreq(c, config.lang))

    if models.embeddings:
        # If WEs have been loaded, include cosine and apsynp metrics.
        cosine_ranked = sorted(candidates, key = lambda c: cosine_sim(tokens[i], c))
        apsynp_ranked = sorted(candidates, key = lambda c: apsyn_sim(tokens[i], c))
        
        overall_ranked = [(c, candidates.index(c) +
                           cosine_ranked.index(c) +
                           apsynp_ranked.index(c) +
                           complex_ranked.index(c)) for c in candidates]

    else:
        # If WEs have not been loaded, only use BERT and frequency.
        overall_ranked = [(c, candidates.index(c) +
                   complex_ranked.index(c)) for c in candidates]

    # Sort candidates based on overall rank.
    overall_ranked = sorted(overall_ranked, key = lambda c: c[1])

    return overall_ranked if overall_ranked else []

def simplify_text(text, bold_highlight=False):
    """Simplifies a given piece of text and returns
    text alongside simplified positions."""
    # Copy tokens to prevent change to original.
    tokens = tokenize(text)
    tokens_copy = tokens.copy()

    # For each copied token
    for i in range(len(tokens_copy)):
        
        # If token is complex, attempt to simplify.
        if suitable_complex_word(tokens_copy[i]):
            candidates = simplify_token(tokens_copy, i)
            
            if candidates:
                if bold_highlight:
                    tokens[i] = "<b>" + candidates[-1][0] + "</b>"
                else:
                    tokens[i] = candidates[-1][0]
                    

    return TreebankWordDetokenizer().detokenize(tokens)
