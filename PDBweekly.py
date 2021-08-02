from rcsbsearch import TextQuery
from rcsbsearch import rcsb_attributes as attrs

# #costruisco le query (attraverso gli attribute che trovo sul sito rcsb search api)
q1 = TextQuery('"sars-cov-2"')
q2 = TextQuery('"antibody"') 
q3 = TextQuery('"spike|receptor binding domain"')
q4 = attrs.exptl.method == "X-RAY DIFFRACTION"
q5 = attrs.rcsb_accession_info.initial_release_date >= "2021-07-27T00:00:00Z"

query = q1 & q2 & q3 & q4 & q5
    # combined using bitwise operators (&, |, ~, etc)


for pdb_code in query("entry"):
    print(pdb_code)

