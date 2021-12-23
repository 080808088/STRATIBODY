import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64
import os, sys
from io import BytesIO

def FILE(a):
        c = pd.read_csv(a)
        dati = c.iloc[:, 2]
        return(dati)

x = [int(b) for b in list(range(101))]
y1 = FILE(sys.argv[3])
y2 = FILE(sys.argv[4])

fig, ax = plt.subplots(1, 1)  # Create a figure and an axes.
fig.suptitle("Affinity Plot" + "_" + str(sys.argv[2]), fontsize=15) # Add a title to the axes.
ax.plot(x, y1, color="green", label="WT")
ax.plot(x, y2, color="red", label="BETA")
ax.set_xlabel('ns')  # Add an x-label to the axes.
ax.set_ylabel('affinity_score')  # Add a y-label to the axes.

prova = sys.argv[1]
if prova == 'y3':
        y3 = FILE(sys.argv[5])
        ax.plot(x, y3, color="blue", label="OMICRON")
else:
        pass
if prova == 'y4':
        y3 = FILE(sys.argv[5])
        ax.plot(x, y3, color="blue", label="OMICRON")
        y4 = FILE(sys.argv[6])
        ax.plot(x, y4, color="orange", label="DELTA")
else:
        pass
if prova == 'y5':
        y3 = FILE(sys.argv[5])
        ax.plot(x, y3, color="blue", label="OMICRON")
        y4 = FILE(sys.argv[6])
        ax.plot(x, y4, color="orange", label="DELTA")
        y5 = FILE(sys.argv[7])
        ax.plot(x, y5, color="purple", label="ALFA")
plt.ylim(0,1)   # Normalize value y.
ax.legend(loc="lower right", title="RBD variant", frameon=False)
plt.savefig("grafico_RBDvariants" + str(sys.argv[2]) + ".png", format = 'png', dpi = 600)
plt.close()
