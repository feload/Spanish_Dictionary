#!/usr/bin/python2
### This program takes Spanish text files as input, strips non-words and punctuation and writes each word to a new line of the output file as long as the word does not already exist in the output file

import string
from os import listdir
from os.path import isfile, join


source_words_dir = "source_words"
source_files = []
testing_file = "source_words/snippet.txt"
word_lst = []


def GetSourceFiles(path):
    """ Function to grab a list of input word files from the source dirctory"""
    for sourcefile in listdir(path):
        if isfile(join(path, sourcefile)):
            source_files.append(sourcefile)

def MakeWordArray(word_file):
    """Take a word file and crate a list containing every every word in the file"""
    with open(word_file, 'rb') as f:
        content = f.read()
        table = string.maketrans(
                string.punctuation,
                ' '*len(string.punctuation))
        content = content.translate(table).lower()
        words = content.split()
        print words
 
 
 #       content = content.translate(None, string.punctuation).lower()
 #       word_lst.append(content.split())
 #       return word_lst
    
    


GetSourceFiles(source_words_dir)
print source_files

MakeWordArray(testing_file)





