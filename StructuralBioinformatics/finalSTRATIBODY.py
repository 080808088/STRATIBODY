import os, sys
import numpy as np
import pandas as pd
import csv
import argparse
import re

def stratibody(f):
        PATH = os.path.join('/home/14802292/finalSTRATIBODY', f)
        a = pd.read_csv(PATH)
        g = pd.DataFrame(a)
        return(g)

mAb1 = stratibody(sys.argv[1])
mAb2 = stratibody(sys.argv[2])
mAb3 = stratibody(sys.argv[3])
mAb4 = stratibody(sys.argv[4])
mAb5 = stratibody(sys.argv[5])
mAb6 = stratibody(sys.argv[6])
mAb7 = stratibody(sys.argv[7])
tot = pd.concat([mAb1, mAb2, mAb3, mAb4, mAb5, mAb6, mAb7])
tot.to_csv(f'STRATIBODY.csv', index=False)
print(tot)

