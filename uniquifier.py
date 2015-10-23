#!/usr/bin/python2
# -*- coding: utf-8 -*-
##This file takes an input text file like a book and writes a new output file where each word only appears once and each word is on a line. 
##I made this because it was taking a long time for the list generator program to iterate over duplicate words in a source file that would never be
##added to the output list.

import nltk, codecs, string
from os import listdir
from os.path import isfile, join

source_file = raw_input("File to uniquify: ")
dup_lst = []
output_lst = []
output_file = ""

##open the user supplied file, split it up into a list of it's words and punctuation
if isfile(source_file):
    with codecs.open(source_file, 'r', "utf-8") as f:
        content = f.read()
        for word in nltk.word_tokenize(content):
            dup_lst.append(word.lower())
else:
    print "File doesn't exist"

##add each word in the starting list to a new list only if that word is not already in the output list.   
#for word in dup_lst:
#    if word not in output_lst and word.isalpha():
#        output_lst.append(word)

##sorting and de-duplicating list
output_lst = sorted(set(dup_lst))

##new variable adding "uniquified" to the name of the origional file
output_file = "uniquified_" + source_file

##writing the de-duplicated list to the new output file
with codecs.open(output_file, "a", "utf-8") as f:
    for word in output_lst:
        f.write(word + "\n")



