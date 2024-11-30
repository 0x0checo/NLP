mport pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

def get_regression(path, x_par, y_par):
    df = pd.read_csv(path)

    df['log_duration'] = np.log(df['duration'])

    sns.regplot(
    data = df, x='log_duration', y=y_par,
    scatter_kws={'s': 10},
    line_kws={'color': 'blue', 'linewidth': 0.8})

    plt.xlabel('Log of ' + x_par)
    plt.ylabel(y_par)

    plt.show()

def main():
    regplot = get_regression(sys.argv[1],'duration', 'surprisal')

if __name__=="__main__":
    main()
~            
