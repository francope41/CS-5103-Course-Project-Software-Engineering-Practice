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

class Word_Stats():
    def __init__(self):
        try:
            self.file_path = sys.argv[1]
        except:
            self.file_path = input("Please type file path: ")
        
        regex_rules = '\s'
        self.patern_separator = re.compile(regex_rules)

        self.just_words_list = []


    def main(self):
        file = open(self.file_path,"r")
        for line in file:
            words_lst = line.split()
            if len(words_lst) >= 1:
                for word in words_lst:
                    self.just_words_list.append(word)
            else:
                continue
        
        word_stats = pd.value_counts(self.just_words_list)

        print(word_stats)

if __name__ == "__main__":
    File_word_stats = Word_Stats()
    File_word_stats.main()