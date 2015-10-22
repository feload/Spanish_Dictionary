#!/usr/bin/python2
# -*- coding: utf-8 -*-
#script to iterate through word list and remove non-interesting words e.g. "aaaaaarrgghh"

import string, codecs

word_file = "sample_words"
out_lst = []
out_file = "cleaned_sorted_spanish_word_list.txt"
multi_letter_lst = []

for letter in list(string.ascii_lowercase):
    multi = letter * 3
    multi_letter_lst.append(multi)
                    
with codecs.open(word_file, 'r', "utf-8") as f:
        content = f.readlines()
        for word in content:
            for multi in multi_letter_lst:
                if multi not in word:
                    out_lst.append(word)
                elif multi in word:
                    break ## I can't get the logic here. Need to think about this some more
                                
                    
print out_lst

#with codecs.open(out_file, "a", "utf-8") as f:
#    for word in out_lst:
#        f.write(word)

 

            
