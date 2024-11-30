import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import sys

def get_histogram(path):
    df = pd.read_csv(path)

    df['rounded_duration'] = np.round(df['duration'])
    counted_duration = Counter(df['rounded_duration'])
    durations = [k for k,v in counted_duration.items() if v > 0 and k != 18]
    freq = [i for i in counted_duration.values() if i > 0]

    plt.figure(figsize=(7, 6))
    plt.bar(durations, freq, edgecolor='blue')
    plt.title('Histogram of Duration')
    plt.xlabel('Duration')
    plt.ylabel('Frequency')

    plt.show()

def main():
    get_histogram(sys.argv[1])

if __name__ == "__main__":
    main()
