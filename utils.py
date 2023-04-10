# Utils contain functions required to fulfill the program requirements

import pandas as pd


# Function to open and read desired file
def read_file(file_path):
    file = open(file_path, "r")
    return file

# Function to check if file is valid


def file_ext_check(file_path):
    if file_path.endswith(".txt"):
        return True
    else:
        return False

# Function to read each line of the file and return list of words


def get_words(file, final_words_list):
    line_counter = 0  # Add counter for line count
    for line in file:
        line_counter = linecount(line_counter)
        words_lst = line.split()
        if len(words_lst) >= 1:
            for word in words_lst:
                final_words_list.append(word)
            else:
                continue

    return final_words_list, line_counter  # Now returns 2 values instead of one

# Function to count each unique word detected and return a pandas array


def count_unique_words(final_words_list):
    word_stats = pd.value_counts(final_words_list)
    return word_stats

# - - - - -  - - - - -  - - - - -  - - - - -  - - - - -  - - - - -  - - - - -  - - - - -  - - - - -  - - - - -
# Requirements for 3 -- 23 -- 2023

# New Feature LineCount


def linecount(count):  # Function in charge of counting the lines
    count += 1
    return count

# New Feature Char Count


def charCount(word):
    return len(word)


# - - - - -  - - - - -  - - - - -  - - - - -  - - - - -  - - - - -  - - - - -  - - - - -  - - - - -  - - - - -
# Requirements for 04 -- 04 -- 2023

# New Feature Word Replacement

def replaceWord(word_init, change_to, words_lst):
    index = 0
    if word_init in words_lst:
        for wrd in words_lst:
            if wrd == word_init:
                words_lst[index] = change_to
            index += 1

        return words_lst

    else:
        print("{} not in text".format(word_init))
        return words_lst
