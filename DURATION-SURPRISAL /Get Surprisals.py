mport nltk
nltk.download('punkt')
from nltk.tokenize import regexp_tokenize
from nltk import sent_tokenize, word_tokenize
from collections import defaultdict
from math import log
import sys

def get_lines(filepath):
    with open(filepath, 'r') as file:
        lines = file.read()

    return lines

def get_unigrams(lst_of_sentences):
    freq_dict = defaultdict(int)
    start = '<s>'
    end = '<e>'

    for sentence in lst_of_sentences:
        freq_dict[start] += 1
        unigrams = word_tokenize(sentence)

        for i in unigrams:
            if i not in freq_dict:
                freq_dict[i] = 1
            else:
                freq_dict[i] += 1
        freq_dict[end] += 1

    return freq_dict

def get_bigrams(lst_of_sentences):
    freq_dict = defaultdict(int)
    start = '<s>'
    end = '<e>'

    for sentence in lst_of_sentences:
        words = word_tokenize(sentence)
        words.append(end)
        words.insert(0, start)

        for i in range(len(words)-1):
            bigram = (words[i], words[i+1])
            if bigram not in freq_dict:
                freq_dict[bigram] = 1
            else:
                freq_dict[bigram] += 1

    return freq_dict

# this function I use to make ten target sentences, since I get them so I comment it
"""
def check_bigrams(sentence, bigram_freq):
    words = word_tokenize(sentence)
    for i in range(len(words) - 1):
        bigram = (words[i], words[i+1])
        if bigram not in bigram_freq:
            return False
        return True
'""
def get_surprisal(p):
    surprisal = -log(p, 2)

    return surprisal

def get_bigram_surprisal(uni_freq_dict, bi_freq_dict):
    bi_surprisal_dict = defaultdict(float)
    V = len(uni_freq_dict)

    for k,v in bi_freq_dict.items():
        first_word_freq = uni_freq_dict.get(k[0], 0)
        f_bigram = v + 1
        f_firstgram = first_word_freq + 1 + V
        con_p = f_bigram / f_firstgram
        bi_surprisal = get_surprisal(con_p)
        bi_surprisal_dict[k] = bi_surprisal

    return bi_surprisal_dict

def get_test_surprisal(sentence, bi_surprisal_dict):
    words = sentence.split()
    total_surprisals = 0
    bigram_count = 0
    for i in range(len(words) - 1):
        bigram = (words[i], words[i+1])
        if bigram in bi_surprisal_dict:
            total_surprisals += bi_surprisal_dict[bigram]
            bigram_count += 1
    return total_surprisals / bigram_count




def main():
    train = get_lines(sys.argv[1])
    train_sentences = sent_tokenize(train)
    unigram_freq = get_unigrams(train_sentences)
    bigram_freq = get_bigrams(train_sentences)
    bi_surprisal_dict = get_bigram_surprisal(unigram_freq, bigram_freq)
    test_sentence = get_lines(sys.argv[2])
    test_surprisal = get_test_surprisal(test_sentence, bi_surprisal_dict)
    print(test_surprisal)
    """
    Following codes I used to make 10 target sentencs now I comment them after g    etting all the sentences
    text_text = get_lines(sys.argv[2])
    text_sentences = sent_tokenize(text_text)

    target_sentences = []
    for sentence in text_sentences:
        if len(word_tokenize(sentence)) >= 15:
            if check_bigrams(sentence, bigram_freq):
                target_sentences.append(sentence)
        if len(target_sentences) >= 10:
            break

    for idx, sentence in enumerate(target_sentences, 1):
        print(f"sentence{idx}:{sentence}")

    """

if __name__ == "__main__":
    main()

