#! /usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
import pickle as pkl
import pandas as pd
import numpy as np
import csv
import argparse
import re
from os import system, getcwd, listdir, makedirs, rename, chdir
import giuseppone as g
import graphic as graph

AB = g.convert(sys.argv[1])
AC = g.convert(sys.argv[2])
col_1 = AB.iloc[:, 0]
col_2 = AC.iloc[:, 0]
tot = pd.DataFrame(list(zip(col_1, col_2)), columns=['AB', 'AC'])
affinity_score = tot.mean(axis=1)

colonna_1 = ["ID" + str(x) for x in list(range(101))]
# #ID

colonna_2 = list(range(101))
# #nanoseconds

g = affinity_score[0:102]
affinity = pd.DataFrame(g)
file_csv = affinity
colonna_3 = file_csv.iloc[:, 0]
print(colonna_3.mean(0))

exp_cond = (f'{sys.argv[3]}-{sys.argv[4]}')
c = [str(exp_cond)]
for z in c:
    z = z.strip()
    colonna_4 = pd.Series(z, index=range(101))
    print(colonna_4)
# #experimental_conditions

df = pd.DataFrame(list(zip(colonna_1, colonna_2, colonna_3, colonna_4)), columns=['ID', 'ns', 'score', 'E.C.'])
print(df)

df.to_csv('STRATIBODY.csv', index=False)

graph.make_graphic('STRATIBODY.csv')
