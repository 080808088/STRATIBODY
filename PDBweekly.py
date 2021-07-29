# #Voglio estrapolare tutti i codici PDB degli anticorpi monoclonali anti sars-cov-2 rilasciati nel PDB nell'ultima settimana (ogni mercoledì)

from rcsbsearch import TextQuery
from rcsbsearch import rcsb_attributes as attrs
import webbrowser

with open('antibody.txt', 'w') as f:

# #costruisco le query (attraverso gli attribute che trovo sul sito rcsb search api)
	q1 = TextQuery('"sars-cov-2"')
	q2 = TextQuery('"antibody"')
	q3 = TextQuery('"spike|receptor binding domain"')
	q4 = attrs.rcsb_accession_info.initial_release_date >= "2021-07-27T00:00:00Z"
	# q5 = TextQuery('"variant"')

	query = q1 & q2 & q3 & q4 #& q5
	# # combined using bitwise operators (&, |, ~, etc)

#	for pdb_code in query("entry"):
#    		print(pdb_code)
	for pdb_code in query("entry"):
		pdb_code = pdb_code.split('\n')
        	# print(pdb_code)
		for l in pdb_code:
			g = l,''
            		#divido ogni codice PDB
			g = ' '.join(g)
           	 	#rendo ogni codice PDB una stringa
			f.write(g)
			print(g)
# #dei PDB trovati mi serve capire se fanno a caso nostro, li cerco su internet e controllo
			check = ("https://rcsb.org/structure/" + g)
			webbrowser.open(check)
