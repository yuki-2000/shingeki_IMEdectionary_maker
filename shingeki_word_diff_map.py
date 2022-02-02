# -*- coding: utf-8 -*-


import difflib
from difflib import SequenceMatcher
import itertools
import pandas as pd
from multiprocessing import Pool
 

def deff_word(i):
    s = SequenceMatcher(None, *i)
    if s.ratio() > 0.80:
        print('類似度：{0}%，\n{1}\n{2}'.format(round(s.ratio()*100,1), i[0],i[1]))
        
        
if __name__ == '__main__':
    df = pd.read_excel('進撃辞書.xlsx',header=None)
    lst = list(df[0])
    p = Pool()
    p.map(deff_word, itertools.combinations(lst, 2))
