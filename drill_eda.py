import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def compute_summary(df):
    numeric_cols = df.select_dtypes(include='number').columns

    summary_dict = {
        'count': [],
        'mean': [],
        'median': [],
        'std': [],
        'min': [],
        'max': []
    }

    for col in numeric_cols:
        summary_dict['count'].append(df[col].count())
        summary_dict['mean'].append(df[col].mean())
        summary_dict['median'].append(df[col].median())
        summary_dict['std'].append(df[col].std())
        summary_dict['min'].append(df[col].min())
        summary_dict['max'].append(df[col].max())

    summary_df = pd.DataFrame(summary_dict, index=numeric_cols)

    os.makedirs('output', exist_ok=True)

    summary_df.to_csv('output/summary.csv')

    return summary_df

def plot_distributions(df, columns, output_path):
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes = axes.flatten()  

    for i, col in enumerate(columns):
        sns.histplot(df[col], kde=True, ax=axes[i])
        axes[i].set_title(col)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def plot_correlation(df, output_path):
    
    numeric_cols = df.select_dtypes(include='number').columns

    corr_matrix = df[numeric_cols].corr(method='pearson')

    plt.figure(figsize=(10, 8))

    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm')

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def summary_stats(df):
    pass

def distribution_plot(df, column):
    pass

def correlation_heatmap(df):
    pass

# ----------------------------------
if __name__ == "__main__":
    df = pd.read_csv("data/sample_sales.csv")
    

    compute_summary(df)
    numeric_cols = df.select_dtypes(include='number').columns[:4]
    plot_distributions(df, numeric_cols, 'output/distributions.png')
    plot_correlation(df, 'output/correlation.png')