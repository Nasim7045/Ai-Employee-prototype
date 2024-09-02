import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr

def perform_summary_analysis(data):
    """Generate summary statistics for the data."""
    summary = data.describe(include='all')
    return summary

def perform_correlation_analysis(data):
    """Calculate the correlation matrix for the data."""
    correlation_matrix = data.corr()
    return correlation_matrix

def perform_regression_analysis(data, target):
    """Perform linear regression analysis on the data."""
    if target not in data.columns:
        raise ValueError(f"Target column '{target}' not found in data.")
    
    X = data.drop(columns=[target])
    y = data[target]
    
    model = LinearRegression()
    model.fit(X, y)
    
    predictions = model.predict(X)
    coefficients = model.coef_
    intercept = model.intercept_
    
    results = {
        'coefficients': coefficients,
        'intercept': intercept,
        'predictions': predictions
    }
    
    return results

def perform_trend_analysis(data):
    """Perform a trend analysis (simple moving average)."""
    if 'Date' not in data.columns:
        raise ValueError("Data must contain a 'Date' column for trend analysis.")
    
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.set_index('Date')
    
    # Calculate moving average
    moving_avg = data.rolling(window=7).mean()  # 7-day moving average as an example
    
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data, label='Original Data')
    plt.plot(data.index, moving_avg, label='7-Day Moving Average', color='red')
    plt.title('Trend Analysis')
    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.legend()
    plt.show()
    
    return moving_avg

def perform_analysis(data, analysis_type, target=None):
    """Perform the specified type of analysis on the data."""
    if analysis_type not in ['summary', 'correlation', 'regression', 'trend']:
        raise ValueError(f"Unsupported analysis type '{analysis_type}'")
    
    if analysis_type == 'summary':
        return perform_summary_analysis(data)
    elif analysis_type == 'correlation':
        return perform_correlation_analysis(data)
    elif analysis_type == 'regression':
        if target is None:
            raise ValueError("Target must be specified for regression analysis.")
        return perform_regression_analysis(data, target)
    elif analysis_type == 'trend':
        return perform_trend_analysis(data)

# Example usage (if running this file directly):
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Perform data analysis")
    parser.add_argument('--file', required=True, help="Path to the data file (CSV or Excel)")
    parser.add_argument('--analysis', required=True, help="Type of analysis to perform")
    parser.add_argument('--target', help="Target column for regression analysis (optional)")
    
    args = parser.parse_args()
    
    # Load data
    if args.file.endswith('.xlsx'):
        data = pd.read_excel(args.file)
    else:
        data = pd.read_csv(args.file)
    
    # Perform analysis
    results = perform_analysis(data, args.analysis, args.target)
    print(results)
