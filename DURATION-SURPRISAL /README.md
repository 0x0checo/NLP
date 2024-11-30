# Replicating the Relationship Between Phonetic Clarity and Surprisal

## Description
This project aims to replicate the well-documented finding that phonetic clarity（Phonetic clarity will here be approximated to duration, that is, the number of milliseconds a specific word has, excluding pauses.）correlates with surprisal. Specifically, when speakers convey less information, their articulation tends to be less clear, while greater clarity is observed when more information is communicated. For a detailed theoretical background, refer to Jaeger and Buz (2017) and the cited references within.

## Data
The analysis is based on the following datasets:
- **Surprisal data**: Using my bigram language model, I get ten well-formed sentences at least 15 words which contained all bigrams can be found in my bigram-surprisal dictionary. 
- **Speech data**: To obtain duration data, I use the MAUS tool for forced alignment of speech and text to produce .csv files containing phoneme durations and write a Python program get_durations.py to extract duration information from the files and calculate the total duration of each word.
- **Sources**:
- Data were sourced from wiki.test.raw file distill from a simple bigram model trained on the wiki.train.raw data.
- To make sure the duration estimates from MAUS are in milliseconds and ake sure every duration is the same as in the output from your Python script, I use Praat to do a sanity check.

## Usage
To replicate the findings:

1. Clone this repository:
   ```bash
   git clone https://github.com/0x0checo/NLP.git
   cd phonetic-clarity-surprisal

