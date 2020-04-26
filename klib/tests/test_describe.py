import pandas as pd
import unittest
from klib.describe import corr_mat

if __name__ == '__main__':
    unittest.main()


class Test_corr_mat(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_corr_df = pd.DataFrame([[1, 0, 3, 4, 'a'],
                                         [3, 4, 5, 6, 'b'],
                                         [5, 4, 2, 1, 'c']],
                                        columns=['Col1', 'Col2', 'Col3', 'Col4', 'Col5'])

        cls.data_corr_list = [1, 2, -3, 4, 5]
        cls.data_corr_target = pd.Series([1, 2, -3, 4, 5], name='Target List')

    def test_output_type(self):
        # Test conversion from pd.io.formats.style.Styler to pd.core.frame.DataFrame
        self.assertIsInstance(type(corr_mat(self.data_corr_df)), type(pd.io.formats.style.Styler))
        self.assertIsInstance(type(corr_mat(self.data_corr_list)), type(pd.io.formats.style.Styler))
        self.assertIsInstance(type(corr_mat(self.data_corr_df, colored=False)), type(pd.DataFrame))
        self.assertIsInstance(type(corr_mat(self.data_corr_list, colored=False)), type(pd.DataFrame))

    def test_output_shape(self):
        # Test for output dimensions
        self.assertEqual(corr_mat(self.data_corr_df).data.shape[0], corr_mat(self.data_corr_df).data.shape[1])
        self.assertEqual(corr_mat(self.data_corr_list).data.shape[0], corr_mat(self.data_corr_list).data.shape[1])
        self.assertEqual(corr_mat(self.data_corr_df, target=self.data_corr_target, colored=False).shape, (4, 1))
        self.assertEqual(corr_mat(self.data_corr_df, target='Col1', colored=False).shape, (3, 1))
