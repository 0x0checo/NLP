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

- **Clone this repository**:
   ```bash
   git clone https://github.com/0x0checo/NLP.git
   cd NLP

## Process Your Data
1. Record ten sentences, convert them to `.wav` format if needed (use tools like `ffmpeg` or `sox`).
2. Upload the `.wav` files to the designated folder.
3. Run the MAUS tool as per the instructions provided in the repository.

## Extract and Analyze Durations
1. Use the `get_durations.py` script to calculate word durations from the `.csv` files generated by MAUS.
2. Compare word durations with surprisal values from the bigram model.

## Validate Results
Perform a sanity check using **Praat** to ensure the durations match between MAUS and Python outputs.

## Installation Requirements
To run the project locally, ensure you have Python installed and the necessary tools like `ffmpeg`, `sox`, and **Praat**. Follow these steps:

1. Clone the repository.
2. Ensure you have access to the MAUS tool and follow its guidelines for processing speech data.

## License 
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code with proper attribution.

