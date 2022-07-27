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

def affinityVersion():
    print("affinity version 0.0.1")

def convert(f):
    with open(f, "rb") as s:
        object = pkl.load(s)

    df = pd.DataFrame(object)
    intermediate = f.split('.')[0]+'.csv'
    file = df.to_csv(intermediate)
    # # convert .pkt to .csv

    result = pd.read_csv(intermediate)
    a = result.dropna()
    affinity_score = a.median(0)   #mi calcola mediana delle colonne
    g = affinity_score[1:102]
    affinity = pd.DataFrame(g)
    file_csv = affinity
    # #selecting and managing data
    return file_csv


