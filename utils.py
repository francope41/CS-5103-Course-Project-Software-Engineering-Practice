#Utils contain functions required to fulfill the program requirements

import pandas as pd


#Function to open and read desired file
def read_file(file_path):
    file = open(file_path,"r")
    return file

#Function to check if file is valid
def file_ext_check(file_path):
    if file_path.endswith(".txt"):
        return True
    else:
        return False

#Function to read each line of the file and return list of words
def get_words(file, final_words_list):
    for line in file:
        words_lst = line.split()
        if len(words_lst) >= 1:
            for word in words_lst:
                final_words_list.append(word)
            else:
                continue

    return final_words_list

#Function to count each unique word detected and return a pandas array
def count_unique_words(final_words_list):
    word_stats = pd.value_counts(final_words_list)
    return word_stats



