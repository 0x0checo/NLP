import json
import os
import re
import sys
import nltk

nltk.download('punkt')
nltk.download('wordnet')
from collections import defaultdict
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

class PositionalInvertedIndexSearch:
    def __init__(self, index_file, normalization_mode = 'none'):
        self.index_file = index_file
        self.index = self.load_index()
        self.normalization_mode = normalization_mode

        # Initialize normalization mode
        self.stemmer = PorterStemmer() if normalization_mode == 'stem' else None
        self.lemmatizer = WordNetLemmatizer() if normalization_mode == 'lemma' else None

    def load_index(self):
        # Open the file at 'json_path' and load the JSON data
        with open(self.index_file, 'r') as file:
            index = json.load(file)
        return index

    def normalization_token(self, token):
        token = token.lower()
        # Switch mode based on input
        if self.normalization_mode == 'stem':
            return self.stemmer.stem(token)
        elif self.normalization_mode == 'lemma':
            return self.lemmatizer.lemmatize(token)
        else:
            return token

    def normalization_phrase(self, phrase):
        tokens = word_tokenize(phrase)
        return [self.normalization_token(token) for token in tokens]

    def search_term(self, phrase):
        # Get normalized terms
        terms = self.normalization_phrase(phrase)
        # Check the number of terms
        if len(terms) == 1:
            term = terms[0]
            if term in self.index:
                return [int(doc_id) for doc_id in self.index[term].keys()]
            else:
            	return []

        elif len(terms) == 2:
            term1, term2 = terms[0], terms[1]
            # Check if two terms both exist
            if term1 not in self.index or term2 not in self.index:
                return []

            # Get files contain term1 or term2
            term1_files = set(self.index[term1].keys())
            term2_files = set(self.index[term2].keys())

            # Get the same files contain both term1 and term2
            same_files = term1_files.intersection(term2_files)

            # Check if two terms are adjacent in the files
            matched_files = []
            for file in same_files:
                term1_pos = self.index[term1][file]
                term2_pos = self.index[term2][file]

                for pos in term1_pos:
                    if pos + 1 in term2_pos:
                        matched_files.append(int(file))
                        break
            return sorted(matched_files)

        else:
            print('This program focuses on phrase queries with one or two (but not three or more) terms!')
            return []


def main():
    if len(sys.argv) < 3:
        print('Lack of arguments(<index_file_path> <normalization_mode>).')
        sys.exit(1)

    # Load all files path
    path = sys.argv[1]
    # Load norm mode
    mode = sys.argv[2]

    if mode not in ['none', 'stem', 'lemma']:
        print('Invalid mode!')
        sys.exit(1)

    # Get file name from json file path
    file_name = os.path.basename(path)
    match = re.search(r'inverted_index_(\w+)\.json', file_name)

    # Check the mode from file name and the mode from argument if matched
    if match:
        # Get mode retrieved from file name
        file_mode = match.group(1)
        if file_mode != mode:
            print(f"Error: The file '{file_name}' is created with '{file_mode}'.")
            print("Please make sure you use the same normalization mode as the index file.")
            sys.exit(1)
    else:
        print(f"Error: Unable to determine the normalization mode from the '{file_name}'")
        sys.exit(1)

    # Create an instance
    pos_idx_search = PositionalInvertedIndexSearch(path, mode)

    while True:
        # Prompt the user for a search term
        query = input("Please enter a phrase to search or 'exit' to end process:")
        # Break the loop if the user types 'exit'
        if query.lower() == 'exit':
            print('Successfully exit!')
            break
        else:
            # Search for the phrase in the index
            res = pos_idx_search.search_term(query)

        if res:
            print(f"Documents {res} contain the phrase '{query}'.")
        else:
            print('Phrase not found!')

if __name__ == '__main__':
    main()
