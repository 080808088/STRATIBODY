# #Per cercare tutti i codici PDB:

import re
PDB = []
with open('mAb.txt', 'r') as f:
	for line in f.readlines():
	# #voglio avere i codici PDB che legano il NTD: (sostituire NTD con ciò di cui ho bisogno, es mAb o RBD)
		if 'NTD' in line:
			line = line.strip()
			# #senza andare a capo
			PDB.append(line)
			# #per ogni riga che contiene la parola ''
			x = re.finditer("7\w{3}|6\w{3}", line)
			# #cerca codici PDB composti da 7 o 6 seguiti da tre altri caratteri
			x = re.finditer("mAb \w+.\w+|mAb \w{2}", line)
			# #se voglio sapere i nomi degli mAb a cui corrispondono i codici PDB trovati /silenziare se voglio codici PDB
			
			for b in x:
				print(b.group())
			# #stampami tutti i codici che hai trovato.
				print(len(PDB))
				# #per vedere quanti sono.