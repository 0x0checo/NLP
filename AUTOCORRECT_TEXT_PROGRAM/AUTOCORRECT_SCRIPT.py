from  collections import defaultdict
import nltk
nltk.download('punkt')
from nltk import word_tokenize
import random

class AutoCorrect:

    def __init__(self, word_list, alpha):
        self.word_list = word_list
        self.alpha = alpha

    # input a word and return a list of words after inserting a character into the word
    def insertion(self, word):

        insert_list = []
        for i in range(len(word)+1):
            for char in self.alpha:
                insert_list.append(word[:i] + char + word[i:]) # insert a character into any position of the word

        return insert_list


    # input a word and return a list of words after deleting a character of the word
    def deletion(self, word):

        delete_list = []
        for i in range(len(word)):
            new_word = word[:i] + word[i+1:] # delete position 'i', remain left characters and keep them in order
            delete_list.append(new_word)

        return delete_list

    # input a word and return a list of words after substituting a character of the word
    def substitution(self, word):

        sub_list = []
        for i in range(len(word)):
            for char in self.alpha:
                sub_list.append(word[:i] + char + word[i+1:])# substitute a character of the word

        return sub_list

    # input a word and return a list of words after swapping two positions of characters of the word
    def swapping(self, word):

        swap_list = []
        for i in range(len(word) - 1):
            new_word = (word[:i] + word[i+1] + word[i] + word[i+2:]) # swap word[i] and word[i+1]
            swap_list.append(new_word)

        return swap_list

    # remove the same suggested words from above four methods, and return a set of unique words
    def allsuggestions(self, word):

        ins = self.insertion(word) # get words after being inserted a character
        delete = self.deletion(word) # get words after being deleted a character
        sub = self.substitution(word) # get words after being substituting a character
        swap = self.swapping(word) # get words after swapping two adjacent words' positions

        result = set(ins+delete+sub+swap) # combine all the words to a set

        return result



# read file and get text
def get_lines(filepath):
    with open(filepath, 'r') as file:
        text = file.read()

    return text

# input a string of text and return a bigram-frequency dictionary,
def bigram_dict(text):
    bigram_freq = defaultdict(int)

    words = word_tokenize(text) # tokenize the text and get a list of words

    # get bigrams
    for i in range(len(words) - 1):
        bigram = (words[i], words[i+1])

        # make corresponding dictionary
        bigram_freq[bigram] += 1


    return bigram_freq

# get the most 3 frequent second words in every bigram for each first word of the bigram
def get_second_word(bi_dict, word):
    # make a list to contain all second words of a bigram
    second_words = [bigram[1] for bigram, freq in sorted(bi_dict.items(),key=lambda x:x[1],reverse=True) if word == bigram[0] ]

    # select top 3 frequent second words if list contain less than 3 words then just return actual number words
    result = []
    for i in range(min(3, len(second_words))):
        result.append(second_words[i])

    return result




def main():
    # prepare corpus and lexicon
    corpus = get_lines('UNv1.0.testset.en')
    word_list = set(get_lines('usenglish-utf8.txt').split())
    # print(word_list)

    # make bigram-frequency dictionary and transform it into a list of tuples
    bi_dict = bigram_dict(corpus)
    # print(bi_dict)

    # make a instance of class Autocorrect
    alpha = "abcdefghijklmnopqrstuvwxyz"
    autocorrect = AutoCorrect(word_list, alpha)

    try:
        while True:
            # get input word
            word = input("Please enter a word: ")

            # check if inout word in lexicon
            if word in word_list:
                suggestions = get_second_word(bi_dict, word)
                if suggestions:
                    print(f"Suggestions for the next word: {suggestions} or you can type in a new word")
                else:
                    # choose 3 random words from lexicon
                    random_words = random.sample(list(word_list), 3)
                    print(f"You can choose three suggested words{random_words} or you can type in a new word")
            else:
                """
                use the method from class AutoCorrect and get all the words have 
                Damerau–Levenshtein edit distance of 1.
                """
                correct_sug = autocorrect.allsuggestions(word)
                # check whether there is any word in the lexicon
                correct_list = [i for i in correct_sug if i in word_list]
                if correct_list:
                    print(f"Maybe you want to type in {correct_list[:3]}?")

                else:
                    # choose 3 random words from lexicon
                    random_words = random.sample(list(word_list), 3)
                    print(f"You can choose three suggested words{random_words} or you can type in a new word")

    # only when user quit the program this loop will end
    except KeyboardInterrupt:
        print('Successfully quit!')


if __name__ == '__main__':
    main()









