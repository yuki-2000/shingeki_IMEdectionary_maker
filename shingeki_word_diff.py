# -*- coding: utf-8 -*-

import difflib
from difflib import SequenceMatcher
import itertools
import pandas as pd



df = pd.read_excel('進撃辞書.xlsx',header=None)
lst = list(df[0])
for i in itertools.combinations(lst, 2):
    s = SequenceMatcher(None, *i)
    if s.ratio() > 0.85:
        print('類似度：{0}%，{1}'.format(round(s.ratio()*100,1), i))
        

