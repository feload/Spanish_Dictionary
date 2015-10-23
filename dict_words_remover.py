#!/usr/bin/python2
# -*- coding: utf-8 -*-
### program to remove any words I already have defined in Matt_dict so I don't needlessly look them up

import codecs

dic = "Matt_dict"
lst_file = "spanish_word_list.txt"
output_file = "sorted_spanish_word_list.txt"
dict_lst = []
working_lst = []
non_dup_lst = []



##create a list of the spanish words in the Matt_dic
with codecs.open(dic, 'r', 'utf=8') as f:
    content = f.readlines()
    for line in content:
        line_lst = line.split()
        if line_lst[0].isalpha():
            dict_lst.append(line_lst[0])
 

##create a list of the words generated from the source files
with codecs.open(lst_file, 'r', 'utf-8') as f:
        content = f.readlines()
        for line in content:
            line_lst = line.split()
            working_lst.append(line_lst[0])

##add any words that appear in the list but not in the dict to a new list
for word in working_lst:
    if word not in dict_lst:
        non_dup_lst.append(word)

##write this new list to new file
with codecs.open(output_file, 'r+', 'utf-8') as f:
    for word in non_dup_lst:
        f.write(word + "\n")
        


            
            
  
            




