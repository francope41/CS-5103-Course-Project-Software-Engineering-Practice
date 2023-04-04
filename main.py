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
        self.char_count_list = []
        # Config for better display of arrays
        pd.set_option('display.colheader_justify', 'center')

    def main(self):
        if file_ext_check(self.file_path):
            file = read_file(self.file_path)  # Read Input file
            # Get every word on a text as a list, get the number of lines in text
            words_lst, num_lines = get_words(file, self.just_words_list)
            # Get the times each word repeats
            word_stats = count_unique_words(words_lst)
            # Go over every unique word in text
            for row in word_stats.index:
                char_counter = charCount(row)
                self.char_count_list.append(char_counter)
            # Build a FDataframe with the words and its count
            fin_Dat = pd.DataFrame(word_stats, columns=["Times Word Repeats"])
            # Add column with the word char counts
            fin_Dat["Char Count"] = self.char_count_list

            # Display info on terminal
            print(" ")
            print("Total Lines in text: {}".format(num_lines))
            print(" ")
            print(fin_Dat)

            #Second requirement Change
            #Ask user for the desired word they want to change
            word_init = input("What word whould you like to change?\n"
                              "Spaces will be ignored, Word inputed is case-sensitive\n ")
            word_init = word_init.replace(" ","")

            #Ask user the desired word they want to put instead          
            word_replacement = input("What do you want to change this word to: (Spaces will be ignored)\n ")
            word_replacement = word_replacement.replace(" ","")

            final_words_list = replaceWord(word_init,word_replacement,words_lst)

            ix = 0
            for wrd in final_words_list:
                if ix%8 == 0:
                    final_words_list.insert(ix,"\n")
                ix+=1
            
            print(' '.join(final_words_list))




        else:
            print('Invalid file extension, .txt file extension required')


if __name__ == "__main__":
    File_word_stats = Word_Stats()
    File_word_stats.main()
