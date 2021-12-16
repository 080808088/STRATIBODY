import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64
import os, sys
from io import BytesIO

a = pd.read_csv(sys.argv[1])
x = [int(b) for b in list(range(101))]
       
y = a.iloc[:, 2]

fig, ax = plt.subplots(1, 1)  # Create a figure and an axes.
ax.plot(x, y)  # Plot some data on the axes.
ax.set_xlabel('ns')  # Add an x-label to the axes.
ax.set_ylabel('affinity_score')  # Add a y-label to the axes.
ax.set_title("Affinity Plot" + "_" + str(sys.argv[2]) + "-" + str(sys.argv[3]))  # Add a title to the axes.
plt.ylim(0,1)   # Normalize value y.

plt.savefig("grafico" + str(sys.argv[2]) + str(sys.argv[3]) + ".png", format = 'png', dpi = 600)
plt.close()
