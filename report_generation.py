import matplotlib.pyplot as plt
import pandas as pd

def generate_report(df, analysis_results, output_path='report.pdf'):
    with open(output_path, 'w') as f:
        f.write("Data Analysis Report\n")
        f.write("====================\n\n")
        f.write(str(analysis_results))
        # Add more details, charts, etc.

def plot_data(df, columns):
    df[columns].plot()
    plt.show()
