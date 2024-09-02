import pandas as pd

def load_data(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.json'):
        return pd.read_json(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format!")

def clean_data(df):
    df = df.dropna()  # Dropping missing values
    df = df.drop_duplicates()  # Dropping duplicates
    # Add more cleaning steps as needed
    return df
