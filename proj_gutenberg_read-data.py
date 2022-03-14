# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 21:06:30 2022

@author: marina

Reads all classic files within '\data\classic_literature'
and generates a dataframe where each row is one book.
Each row is composed of 3 values (columns):
    text_id: id from Project Gutenberg
    text_type: 'C' - for Classic
    text: pre-cleaned text
"""

import pandas as pd
import os
import re

#fileName = '.\\data\\classic_literature\\45.txt'
directory = '.\\data\\classic_literature'
text_type = 'C'

classic_df = pd.DataFrame(columns=['id', 'type', 'text'])

for filename in os.listdir(directory):
    with open(directory+"\\"+filename, 'r') as file:
        text_id = os.path.basename(filename).rsplit('.',1)[0]

        if text_id != "README":
            corpus = file.read().lower().replace('chapter', '').replace('\n', '')
            corpus = re.sub('\W+',' ', corpus ) #Remove special characters and punctuation
            #corpus = re.sub('[!,*)@#%(&$_?^]·.-;', ' ', corpus)
            classic_df.loc[len(classic_df.index)] = [text_id, text_type, corpus]


# For testing purposes
# with open('.\\data\\classic_literature\\45.txt', 'r') as file:
#         corpus = file.read().lower().replace('chapter', '').replace('\n', '')
#         text_id = 45
#         corpus = re.sub('\W+',' ', corpus ) #Remove special characters and punctuation
#         classic_df.loc[len(classic_df.index)] = [text_id, text_type, corpus]

# test = '33 +´+f . ;-, %&/7 kshew dwij   oerj eo1|?ªª:eed .'
# test = re.sub('\W+',' ', corpus )
# print(test)
