import os, sys
import numpy as np
import pandas as pd
import csv
import argparse
import re

def stratibody(f):
	PATH = os.path.join('/home/14802292/', f)
	a = pd.read_csv(PATH)
	g = pd.DataFrame(a)
	return(g)

WT = stratibody(sys.argv[2])
Alpha = stratibody(sys.argv[3])
Beta = stratibody(sys.argv[4])
Delta = stratibody(sys.argv[5])
Omicron = stratibody(sys.argv[6])

tot = pd.concat([WT, Alpha, Beta, Delta, Omicron])
tot.to_csv(f'STRATIBODY_{sys.argv[1]}.csv', index=False)
print(tot)
