from simplifier import simplifier
import csv

def read_eval_index_dataset(data_path, is_label=True):

    sentences = []
    mask_words = []
    mask_labels = []

    with open(data_path, "r", encoding='ISO-8859-1') as reader:
        while True:
            line = reader.readline()
            
            if not line:
                break
            
            sentence,words = line.strip().split('\t',1)
            mask_word,labels = words.strip().split('\t',1)
            label = labels.split('\t')
                
            sentences.append(sentence)
            mask_words.append(mask_word)
                
            one_labels = []
            for la in label[1:]:
                if la not in one_labels:
                    la_id,la_word = la.split(':')
                    one_labels.append(la_word)
                
                #print(mask_word, " ---",one_labels)
            mask_labels.append(one_labels)
            
    return sentences, mask_words, mask_labels

def evaulation_pipeline_scores(substitution_words,source_words,gold_words):

    instances = len(substitution_words)
    precision = 0
    accuracy = 0
    changed_proportion = 0

    for sub, source, gold in zip(substitution_words,source_words,gold_words):
        #print(str(sub) + " - " + source)
        if sub == source or (sub in gold):
            precision += 1
        if sub != source and (sub in gold):
            accuracy += 1
        if sub != source:
            changed_proportion += 1

        #if sub != source and (sub not in gold):
            #print("Source: " + source + ", Sub: " + sub + ", Gold: " + str(gold))

    return precision/instances,accuracy/instances,changed_proportion/instances

data = read_eval_index_dataset("simplifier/benchmark/BenchLS.txt")

subs = []
for sentence, word in zip(data[0], data[1]):
    sentence = sentence.lower()
    tokens = sentence.split()
    index = tokens.index(word.lower())

    simplified_tokens = simplifier.simplify_token(tokens, index)
    #print(simplified_tokens)
    subs.append(simplified_tokens[-1][0])

results = evaulation_pipeline_scores(subs, data[1], data[2])
    
# Calculate and display Potential, Precision and Recall for sub generation.
print("\nPrecision: " + str(results[0]))
print("Accuracy: " + str(results[1]))
print("Changed Proportion: " + str(results[2]))
