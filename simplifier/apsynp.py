import math
from gensim.models import KeyedVectors

POWER = 0.4
BASE_POWER = 0.95
formula = 0

def detection(w1, w2, word_vectors):

    # First an second word embeddings.
    v1 = word_vectors.get_vector(w1.lower())
    v2 = word_vectors.get_vector(w2.lower())

    # First and second word embedding features with index.
    v1_mat = [(1, i, v) for i, v in enumerate(v1)]
    v2_mat = [(1, i, v) for i, v in enumerate(v2)]

    # Rank word features using APSyn algorithm.
    score_original, score_power = APSyn(v1_mat, v2_mat)

    # Store results in array and return.
    result = [score_original, score_power]

    return result

def sort_by_value_get_col(mat):

    # Sort by vector value (vector value ex. -0.098393)
    sorted_tuples = sorted(mat, key=lambda x: x[2], reverse=True)

    if len(sorted_tuples) == 0:
        return []

    rows, columns, values = zip(*sorted_tuples)
    return columns

def APSyn(x_row, y_row):

    # Sort first word embedding vectors by feature value.
    y_contexts_cols = sort_by_value_get_col(y_row)
    y_context_rank = { c : i + 1 for i, c in enumerate(y_contexts_cols) }

    # Sort second word embedding vectors by feature value.
    x_contexts_cols = sort_by_value_get_col(x_row)
    assert len(x_contexts_cols) == len(y_contexts_cols)
    x_context_rank = { c : i + 1 for i, c in enumerate(x_contexts_cols) }

    # Average of 1/(rank(w1)+rank(w2)/2) for every intersected feature among the top N contexts
    intersected_context = set(y_contexts_cols).intersection(set(x_contexts_cols))

    # Get original and score power 
    score_original = sum([2.0 / (x_context_rank[c] + y_context_rank[c]) for c in intersected_context]) #Original
    score_power = sum([2.0 / (math.pow(x_context_rank[c], POWER) + math.pow(y_context_rank[c], POWER)) for c in intersected_context])

    # Return original score and score power.
    return score_original, score_power

if __name__ == '__main__':

    # Word to find related words for.
    target_word = "abundant" 
    # Find top 10 similar words according to cosine similarity.
    cosine_results = word_vectors.most_similar(target_word, topn = 20)
    # Rank top 10 similar words according to APsynP similarity.
    apsynp_results = [(result[0], detection(target_word, result[0])[1]) for result in cosine_results]
    apsynp_results = sorted(apsynp_results, key = lambda result: result[1], reverse = True)

    # Print cosine results.
    print("\nCosine Results:\n")
    for result in cosine_results[:10]:
        print(result)

    #Print APSynP results.
    print("\nAPsynP Results:\n")
    for result in apsynp_results[:10]:
        print(result)
    
