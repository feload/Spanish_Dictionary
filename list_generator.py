#!/usr/bin/python2
# -*- coding: utf-8 -*-
### This program takes Spanish text files as input, strips non-words and punctuation and writes each word to a new line of the output file as long as the word does not already exist in the output file

import nltk, codecs, string
from os import listdir
from os.path import isfile, join


source_words_dir = "source_words"
source_files = []
testing_file = "source_words/snippet.txt"
dirty_word_lst = []
clean_word_lst = []

#Generate list of spanish word files
for sourcefile in listdir(source_words_dir):
    if isfile(join(source_words_dir, sourcefile)):
        source_files.append(join(source_words_dir, sourcefile))

#Read files in utf-8 and append all words and punctuation to list
with codecs.open(testing_file, 'r', "utf-8") as f:
    content = f.read()
    for word in nltk.word_tokenize(content):
        dirty_word_lst.append(word.lower())
    
for word in dirty_word_lst:
    print word + "\n"

   



    





