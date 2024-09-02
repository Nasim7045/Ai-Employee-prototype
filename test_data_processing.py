import unittest
import pandas as pd
from scripts.data_processing import load_data, clean_data

class TestDataProcessing(unittest.TestCase):

    def test_load_data_csv(self):
        df = load_data('data/sample_data.csv')
        self.assertIsInstance(df, pd.DataFrame)

    def test_load_data_json(self):
        df = load_data('data/sample_data.json')
        self.assertIsInstance(df, pd.DataFrame)

    def test_clean_data(self):
        raw_data = {'A': [1, 2, None, 4], 'B': [None, 2, 2, 4]}
        df = pd.DataFrame(raw_data)
        cleaned_df = clean_data(df)
        self.assertEqual(cleaned_df.isnull().sum().sum(), 0)  # No missing values
        self.assertEqual(len(cleaned_df), 2)  # Two rows should remain after cleaning

if __name__ == '__main__':
    unittest.main()
