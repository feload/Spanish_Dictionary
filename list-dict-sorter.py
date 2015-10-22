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




with codecs.open(dic, 'r', 'utf=8') as f:
    content = f.readlines()
    for line in content:
        line_lst = line.split()
        if line_lst[0].isalpha():
            dict_lst.append(line_lst[0])
 

with codecs.open(lst_file, 'r', 'utf-8') as f:
        content = f.readlines()
        for line in content:
            line_lst = line.split()
            working_lst.append(line_lst[0])
 
for word in working_lst:
    if word not in dict_lst:
        non_dup_lst.append(word)

with codecs.open(output_file, 'r+', 'utf-8') as f:
    for word in non_dup_lst:
        f.write(word + "\n")
        


            
            
  
            




