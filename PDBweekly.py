# #Voglio estrapolare tutti i codici PDB degli anticorpi monoclonali anti sars-cov-2 rilasciati nel PDB nell'ultima settimana (ogni mercoledì)

from rcsbsearch import TextQuery
from rcsbsearch import rcsb_attributes as attrs

# #costruisco le query (attraverso gli attribute che trovo sul sito rcsb search api)
q1 = TextQuery('"sars-cov-2"')
q2 = TextQuery('"antibody"') 
q3 = TextQuery('"spike|receptor binding domain"')
q4 = attrs.rcsb_accession_info.initial_release_date >= "2021-06-15T00:00:00Z"
# q5 = TextQuery('"variant"')
# q5 = attrs.entity_src_gen.pdbx_host_org_scientific_name != "homo sapiens"

query = q1 & q2 & q3 & q4 #& q5
# combined using bitwise operators (&, |, ~, etc)
for pdb_code in query("entry"):
    print(pdb_code)
# #Per controllare i codici PDB trovati

# PDB = []
# PDB.append(results)
# PDB_str = []
# PDB_str = ''.join(PDB)

# print(PDB_str)


# with open('weeklyresults.txt', 'w') as f:
#    f.write(results)


# import webbrowser
# key = PDB_str   
# check = ("https://rcsb.org/structure/" + key)
# webbrowser.open(check)
# print(key)
       
# #dei PDB trovati mi serve capire se fanno a caso nostro, li cerco su internet e controllo
# import webbrowser
 # key = PDB.append()
 #    check = ("https://rcsb.org/structure/" + key)
 #    webbrowser.open(check)
