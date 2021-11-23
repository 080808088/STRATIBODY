#! /usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64
import os, sys
from io import BytesIO

def make_graphic(f):
	a = pd.read_csv(f)
	x = [int(b) for b in list(range(101))]
        
	y = a.iloc[:, 2]

	fig, ax = plt.subplots(1, 1)  # Create a figure and an axes.
	ax.plot(x, y)  # Plot some data on the axes.
	ax.set_xlabel('ns')  # Add an x-label to the axes.
	ax.set_ylabel('affinity_score')  # Add a y-label to the axes.
	ax.set_title("Affinity Plot" + "_" + str(sys.argv[3]) + "-" + str(sys.argv[4]))  # Add a title to the axes.

	out = plt.savefig("grafico.png", format = 'png', dpi = 600)
	out = plt.close()
	return(out)
