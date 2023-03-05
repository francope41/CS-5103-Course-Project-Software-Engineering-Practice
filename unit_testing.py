import unittest
from utils import *


class Test_read_file(unittest.TestCase):
    def test_corr_file(self):
        file_path = "test_file.txt"
        self.assertEqual(str(type(read_file(file_path))), "<class '_io.TextIOWrapper'>")
        
    def test_bad_file(self):
        file_path = 2
        with self.assertRaises(ValueError):
            read_file(file_path)

class Test_file_ext_check(unittest.TestCase):
    def test_correct_ext(self):
        file_path = "test_file.txt"
        self.assertTrue(file_ext_check(file_path))

    def test_wrong_ext(self):
        file_path = "test_file.pdf"
        self.assertFalse(file_ext_check(file_path))

class Test_get_words(unittest.TestCase):
    def test_getting_words(self):
        file_path = "test_file.txt"
        final_words_list = []
        file = read_file(file_path)
        self.assertEqual(type(get_words(file,final_words_list)),type(final_words_list))

class Test_count_unique_words(unittest.TestCase):
    def test_count(self):
        file_path = "test_file.txt"
        final_words_list = []
        file = read_file(file_path)
        final_words_list = get_words(file,final_words_list)
        self.assertEqual(type(count_unique_words(final_words_list)),pd.Series)

    def test_count_empty(self):
        final_words_list = []
        self.assertEqual(type(count_unique_words(final_words_list)),pd.Series)

class Test_display_results(unittest.TestCase):
    def test_display(self):
        file_path = "test_file.txt"
        final_words_list = []
        file = read_file(file_path)
        final_words_list = get_words(file,final_words_list)
        word_Stats = count_unique_words(final_words_list)
        self.assertEqual(word_Stats[0],8)
        self.assertEqual(len(word_Stats),87)

if __name__ == '__main__':
    unittest.main()