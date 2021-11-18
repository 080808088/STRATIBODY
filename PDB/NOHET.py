import os
import sys
import re
import argparse
from Bio import PDB
from Bio.PDB import Select, PDBIO
from Bio.PDB.PDBParser import PDBParser

pdb = (f'{sys.argv[1]}')

with open(pdb, "r") as inputFile,open("pdb_NOHET.pdb","w") as outFile:
    for line in inputFile:
        if not line.startswith("HETATM"):
            outFile.write(line) 

