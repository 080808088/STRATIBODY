import os
import sys
import re
import argparse
from Bio import PDB
from Bio.PDB import Select, PDBIO
from Bio.PDB.PDBParser import PDBParser

parser = argparse.ArgumentParser()
parser.add_argument("-pdb", type=str, help="structure to clean")
args = parser.parse_args()

if args.pdb:
        with open(f'{args.pdb}', "r") as inputFile,open("pdb_NOHET.pdb","w") as outFile:
	        for line in inputFile: 
        	        if not line.startswith("HETATM"): 
                	        outFile.write(line) 

