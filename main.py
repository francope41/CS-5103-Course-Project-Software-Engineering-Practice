# CS 5103 Course Project: Software Engineering Practice
# By Eulises Franco
# String and Words Topic
# Program will perform  word statistics of a given document (string) Initial requirement is to:
# Count the frequency of each word.
# Code supports combinations of space, tab, and newline characters as separators
#
# Import required packages
import pandas as pd
import re
import sys
from utils import *

class Word_Stats():
    def __init__(self):
        try:
            self.file_path = sys.argv[1]
        except:
            self.file_path = input("Please type file path: ")
            
        self.just_words_list = []


    def main(self):
        if file_ext_check(self.file_path):
            file = read_file(self.file_path)
            words_lst = get_words(file,self.just_words_list)
            word_stats = count_unique_words(words_lst)
            print(word_stats)

        else:
            print('Invalid file extension, .txt file extension required')


if __name__ == "__main__":
    File_word_stats = Word_Stats()
    File_word_stats.main()