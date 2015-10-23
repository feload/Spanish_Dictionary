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
symbol_lst = []
output_lst = []
output_file = "output.txt"

#Generate list of spanish word files
for sourcefile in listdir(source_words_dir):
    if isfile(join(source_words_dir, sourcefile)):
        source_files.append(join(source_words_dir, sourcefile))

#Read files in utf-8 and append all words and punctuation to list
for item in source_files:
    print item
    with codecs.open(item, 'r', "utf-8") as f:
        content = f.read()
        for word in nltk.word_tokenize(content):
            dirty_word_lst.append(word.lower())
        
#Populate punctuation symbol list
for symbol in string.punctuation:
    symbol_lst.append(symbol)

#Remove punctuation
for symbol in symbol_lst:
    print symbol
    if symbol in dirty_word_lst:
        dirty_word_lst.remove(symbol)

#Add word to output list if is is not already there and is not a number
#for word in dirty_word_lst:
#    if word not in output_lst and word.isalpha():
#        output_lst.append(word)

output_lst = sorted(set(dirty_word_lst))

#Sort word list
#output_lst.sort()

#write output list to output file one word to a line
with codecs.open(output_file, "r+", "utf-8") as f:
    for word in output_lst:
        f.write(word + "\n")







  



    





