import unittest
import pandas as pd
from scripts.report_generation import generate_report

class TestReportGeneration(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [2, 3, 4, 5, 6]
        })

    def test_generate_report(self):
        analysis_results = {'A': 1, 'B': 2}
        generate_report(self.df, analysis_results, output_path='report_test.pdf')
        with open('report_test.pdf', 'r') as file:
            content = file.read()
        self.assertIn("Data Analysis Report", content)

if __name__ == '__main__':
    unittest.main()
