import os, sys
import pandas as pd
import numpy as np
import csv
import argparse
import re
from os import system, getcwd, listdir, makedirs, rename, chdir

colonna_1 = ["ID" + str(x) for x in list(range(101))]
# # #ID

colonna_2 = list(range(101))
# # #nanoseconds
# def triplicate(l):

def triplicate(f):
	PATH = os.path.join('/home/14802292', f)
	a = pd.read_csv(PATH)
	g = a.iloc[:,2]
	return(g)

exp1 = triplicate(sys.argv[1])
exp2 = triplicate(sys.argv[2])
exp3 = triplicate(sys.argv[3])

df = pd.DataFrame(list(zip(exp1, exp2, exp3)), columns=['1', '2', '3'])
colonna_3 = df.mean(1)

exp_cond = (f'{sys.argv[4]}-{sys.argv[5]}')
c = [str(exp_cond)]
for z in c:
    z = z.strip()
    colonna_4 = pd.Series(z, index=range(101))
# #experimental_conditions

df = pd.DataFrame(list(zip(colonna_1, colonna_2, colonna_3, colonna_4)), columns=['ID', 'ns', 'score', 'E.C.'])
print(df)

df.to_csv(f'STRATIBODY_{sys.argv[4]}-{sys.argv[5]}.csv', index=False)

print('media affinity score=' + str(colonna_3.mean(0)))
