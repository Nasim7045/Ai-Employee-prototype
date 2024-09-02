import sys
print(sys.path)
import os
from data_processing import load_data, clean_data
from analysis_engine import linear_regression_analysis, kmeans_clustering, decision_tree_classification
from report_generation import generate_report
import argparse

# Define the path to the data folder
DATA_FOLDER = 'data/'

def main():
    parser = argparse.ArgumentParser(description="AI Employee for Data Analysis and Reporting")

    # Arguments for file selection and analysis
    parser.add_argument('--file', type=str, required=True, help="Data file name (CSV, JSON, Excel)")
    parser.add_argument('--analysis', type=str, required=True, help="Type of analysis: linear_regression, kmeans, decision_tree")
    parser.add_argument('--target', type=str, help="Target column for analysis (Required for linear_regression and decision_tree)")

    args = parser.parse_args()

    # Construct file path from data folder
    file_path = os.path.join(DATA_FOLDER, args.file)

    # Load and clean data
    try:
        df = load_data(file_path)
    except ValueError as e:
        print(f"Error: {e}")
        return

    df = clean_data(df)

    # Perform analysis
    if args.analysis == 'linear_regression':
        if not args.target:
            print("Error: --target argument is required for linear_regression analysis.")
            return
        results = linear_regression_analysis(df, args.target)
        print(f"Linear Regression Results:\nCoefficients: {results[0]}\nIntercept: {results[1]}")

    elif args.analysis == 'kmeans':
        results = kmeans_clustering(df, n_clusters=3)
        print(f"K-Means Clustering Results: {results}")

    elif args.analysis == 'decision_tree':
        if not args.target:
            print("Error: --target argument is required for decision_tree analysis.")
            return
        results = decision_tree_classification(df, args.target)
        print(f"Decision Tree Feature Importances: {results}")

    else:
        print(f"Error: Unsupported analysis type '{args.analysis}'.")
        return

    # Generate a report
    output_report = f'report_{args.analysis}.pdf'
    generate_report(df, results, output_report)
    print(f"Report generated successfully: {output_report}")

if __name__ == '__main__':
    main()
