import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(df, column, bins=30, kde=True, figsize=(8, 5), color=None):
    """
    Plots the distribution of a single numerical column from a DataFrame with an optional legend.
    
    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the numeric column to plot.
        bins (int): Number of bins for the histogram.
        kde (bool): Whether to plot the KDE (kernel density estimate).
        figsize (tuple): Size of the plot (width, height).
        color (str or None): Optional color for the plot.
    """
    plt.figure(figsize=figsize)
    plot = sns.histplot(df[column], bins=bins, kde=kde, color=color, label='Histogram')

    if kde:
        plt.legend(labels=['Kernel Density Estimate', 'Histogram'])  # KDE = Kernel Density Estimate
    else:
        plt.legend(labels=['Histogram'])

    plt.title(f'Distribution of {column}', fontsize=14)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()
