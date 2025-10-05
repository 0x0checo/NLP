import glob
import json
import os
import nltk
import sys

nltk.download('punkt')
nltk.download('wordnet')
from collections import defaultdict
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer


class PositionalInvertedIndex:

    def __init__(self, file_list, normalization_mode = 'none'):
        # Initialize data structures for the inverted index
        self.file_list = file_list
        self.positional_index = defaultdict(lambda: defaultdict(list)) # Map term to a dictionary
        self.normalization_mode = normalization_mode

        # Initialize normalization mode
        self.stemmer = PorterStemmer() if normalization_mode == 'stem' else None
        self.lemmatizer = WordNetLemmatizer() if normalization_mode == 'lemma' else None


    @staticmethod
    def get_data(path):
        # Open and read the contents of the file at 'path'
        with open(path, 'r') as file:
            return file.read()

    @staticmethod
    def get_tokens(text):
        # Tokenize the text using nltk.word_tokenize
        return word_tokenize(text)

    def normalization_token(self, token):
        token = token.lower()
        # Switch mode based on input
        if self.normalization_mode == 'stem':
            return self.stemmer.stem(token)
        elif self.normalization_mode == 'lemma':
            return self.lemmatizer.lemmatize(token)
        else:
            return token

    def build_inverted_indexes(self):
        # Assign a unique ID
        for file in self.file_list:
            file_id = int(file.split('.')[-2].split('/')[-1])

            texts = self.get_data(file)
            tokens = self.get_tokens(texts)

            # Store positions of terms
            for position, token in enumerate(tokens):
                # Normalize token for different modes
                normalized_token = self.normalization_token(token)
                self.positional_index[normalized_token][file_id].append(position)

def main():
    # Command line for different modes
    mode = 'none'

    if len(sys.argv) > 1:
        mode = sys.argv[1]

    if mode not in ['none', 'stem', 'lemma']:
        print("Invalid mode! Defaulting to 'none'")
        mode = 'none'

    # Create a relative path
    base_dir = os.path.join('..')

    # Get all files in the directory
    file_paths = glob.glob(os.path.join(base_dir, 'reuters', '*.txt'))

    # Create an PositionalInvertedIndex instance
    pos_idx = PositionalInvertedIndex(file_paths, mode)

    # Build the inverted index
    pos_idx.build_inverted_indexes()

    # Make sure 'index' dir exists
    index_dir = os.path.join(base_dir, 'index')
    os.makedirs(index_dir, exist_ok=True)

    # Write the result to a JSON file
    output_file_path = os.path.join(index_dir, f'inverted_index_{mode}.json')
    with open(output_file_path, 'w') as file:
        json.dump(pos_idx.positional_index, file, indent=2)

    print(f'Successfully create inverted_index_{mode} json file!')

if __name__ == '__main__':
    main()



