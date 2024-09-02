import unittest
import pandas as pd
from scripts.analysis_engine import linear_regression_analysis, kmeans_clustering, decision_tree_classification

class TestAnalysisEngine(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [2, 3, 4, 5, 6],
            'C': [3, 4, 5, 6, 7]
        })

    def test_linear_regression(self):
        coef, intercept = linear_regression_analysis(self.df, 'C')
        self.assertEqual(len(coef), 2)  # Two features should be in the model
        self.assertIsInstance(intercept, float)

    def test_kmeans_clustering(self):
        labels = kmeans_clustering(self.df, 2)
        self.assertEqual(len(labels), 5)  # Should return a label for each row

    def test_decision_tree_classification(self):
        feature_importances = decision_tree_classification(self.df, 'C')
        self.assertEqual(len(feature_importances), 2)  # Two features should be important

if __name__ == '__main__':
    unittest.main()
