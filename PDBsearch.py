from rcsbsearch import TextQuery
from rcsbsearch import rcsb_attributes as attrs
import re
import webbrowser
from pypdb import *
from Bio import *

with open('antibody.txt', 'w') as f:
# #costruisco le query (attraverso gli attribute che trovo sul sito rcsb search api)
    q1 = TextQuery('"sars-cov-2"')
    q2 = TextQuery('"antibody"') 
    q3 = TextQuery('"spike|receptor binding domain"')
    q5 = attrs.exptl.method == "X-RAY DIFFRACTION"
    #q6 = TextQuery('"nanobody"')
    #q4 = TextQuery('"humanized"')
    #q4 = attrs.rcsb_accession_info.initial_release_date >= "2021-07-27T00:00:00Z"

    query = q1 & q2 & q3 & q5
    # combined using bitwise operators (&, |, ~, etc)


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
            print(type(g))
            # check = ("https://rcsb.org/structure/" + g)
            # webbrowser.open(check)

# info = get_info()
# print(info)
