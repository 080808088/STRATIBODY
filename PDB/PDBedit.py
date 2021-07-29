import os
import sys
import re
from Bio import PDB
from Bio.PDB import Select, PDBIO
from Bio.PDB.PDBParser import PDBParser    

class SelectChains(PDB.Select):
	def __init__(self, chain_letters):
		self.chain_letters = chain_letters

	def accept_chain(self, chain):
		return (chain.get_id() in self.chain_letters)


chains_letters = ['E','H','L']
chains = ", ".join(chains_letters)
p = PDBParser(PERMISSIVE=1)
with open("6zcz.pdb", "r+") as pdb_file:
	structure = p.get_structure(pdb_file, pdb_file)
	pdb_chain_file = '6zcz_file_chains.pdb'.format(chains)
	io_w_no_h = PDBIO()
	io_w_no_h.set_structure(structure)
	io_w_no_h.save('{}'.format(pdb_chain_file), SelectChains(chains))

with open("6zcz_file_chains.pdb", "r") as inputFile,open("6zcz_NOHET.pdb","w") as outFile:
        for line in inputFile:
                if not line.startswith("HETATM"):
                        outFile.write(line)
