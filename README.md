# STRATIBODY_Sars-Cov-2
## STRuctural stAbility and anTIBODY effectiveness against spike sars-cov-2 protein
### prerequisites
- Suite **Shrodinger** installed. [link for download](https://www.schrodinger.com/downloads/releases);
- **GROMACS 2021.2** installed. [link for download](https://manual.gromacs.org/documentation/2021.2/download.html);
- Ettore Lo Cascio project: [gitlab link](https://gitlab.com/Ekein/htmd)

### Getting started
PDB code available at [RCSB:PDB](rcsb.org).

Use *rcsbSEARCH.json* to check realeasing of new PDBs of mAb against SC2 RBD. 

Here, PDBcode selected for validation analysis:
- **_7C01_** -> *Ly-cov016 (CB6)* _Etesevimab_

- **_7KMG_** -> *Ly-Cov555* _Bamlanivimab_

- **_7L7D_** -> *AZD8895* _Tixagevimab_

- **_7L7E_** -> *AZD1061* _Cilgavimab_

- **_6ZCZ_** -> *EY6A*

- **_7CM4_** -> *CT-P59* _Regdanvimab_

- **_7R6W_** -> *S309* _Sotrovimab_
Variants Sars-Cov-2 monitored by WHO [World Health Organization](https://www.who.int/en/activities/tracking-SARS-CoV-2-variants/)

LINEAGE | RBD mutation

_Alpha_ (B.1.1.7): N501Y

_Beta_ (B.1.351): K417N,E484K,N501Y

_Delta_ (B.1.617.2): L452R,T478K

_Omicron_ (B.1.1.529.1): G339D, S371L, S373P, S375F, K417N, N440K, G446S, S477N, T478K, E484A, Q493R, G496S, Q498R, N501Y, Y505H

## WORKFLOW
### 1. PDB download 
`/apps/schrodinger/2021.2/run utilities/getpdb PDBcode`
### 2. Visualize PDB on maestro interface
Use tool ‘change atom property’ in order to assign correct chain name at Spike and mAb:
- **7C01** :

	 	- chain A Spike-RBD -> chain A
		
		- chain H Heavy Fab -> chain B

		- chain L Light Fab -> chain C

- **7KMG** :

	 	- chain C Spike-RBD -> chain A

		- chain A Heavy Fab -> chain B

		- chain B Light Fab -> chain C

- **7L7D** :

	 	- chain E Spike-RBD -> chain A

		- chain H Heavy Fab -> chain B

		- chain L Light Fab -> chain C

- **7L7E** :

	 	- chain G Spike-RBD -> chain A

		- chain E Heavy Fab -> chain B

		- chain F Light Fab -> chain C

- **6ZCZ** :

	 	- chain E Spike-RBD -> chain A

		- chain H Heavy Fab -> chain B

		- chain L Light Fab -> chain C

- **7CM4** :

	 	- chain A Spike-RBD -> chain A

		- chain H Heavy Fab -> chain B

		- chain L Light Fab -> chain C

- **7R6W** :

		- chain R Spike-RBD -> chain A

		- chain A Heavy Fab -> chain B
		
		- chain B Light Fab -> chain C
### 3. Clean PDB from HETATM
If it is necessary delete others chains than A,B,C with:

`python3 ~/stratibody_sars-cov-2/PDB/PDBchainsclean.py –pdb filePDB.pdb` -> *pdb_NOHET.pdb*

If only chains A,B,C are in PDB file launch: 

`python3 ~/stratibody_sars-cov-2/PDB/NOHET.py –pdb filePDB.pdb` -> *pdb_NOHET.pdb*
### 4. Protein PREParation
`/apps/schrodinger/2021.2/utilities/prepwizard pdb_NOHET.pdb pdbPREP.pdb -fillsidechains -fillloops -D -WAIT`
### 5. Molecular Dynamic Simulation
`cd ~/htmd`

`git switch bea_working_analysis`

If simulation is performed with a mutated RBD, run the following command before MDsimulation: 

`python3 ~/htmd/mutation.py -i pdbPREP.pdb -r "A-417,A-452,A-478" -a "THR,ARG,LYS" -o fileoutput.pdb`

MDsimulation:

`python3 ~/htmd/protein.py -s ~/path_to/pdbPREP.pdb -nt 24 -ns 100 -ff oplsaa -d 1 -bt dodecahedron -ntmpi -trj`

For further information `python3 ~/htmd/protein.py -h`

### 6. Molecular Dynamic Analysis
`python3 ~/htmd/native.py -tpr MD.tpr -xtc trjadj.xtc -method switch_function -sel_A "segid A" -sel_B "segid B"` -> *segid B_with_segid A.pkl*; *contacts_of_segid B_with_segid A.png*

`python3 ~/htmd/native.py -tpr MD.tpr -xtc trjadj.xtc -method switch_function -sel_A "segid A" -sel_B "segid C"` -> *segid C_with_segid A.pkl*; *contacts_of_segid C_with_segid A.png*

`python3 ~/stratibody_sars-cov-2/analysisMD.py segid\ B_with_segid\ A.pkl segid\ C_with_segid\ A.pkl RBDtype mAbname` -> *STRATIBODY.csv*; *grafico.png*
### 7. Data Analysis
Avarage of the experiments in triplicate: 

`python3 ~/stratibody_sars-cov-2/STRATIBODYtot.py directory_exp1/STRATIBODY.csv directory_exp2/STRATIBODY.csv directory_exp3/STRATIBODY.csv RBDtype mAbname` -> *STRATIBODY_RBDtype-mAbname.csv* ; *graficoRBDtypemAb.png*

Cumulative graph of the antibody effectiveness against RBD variants:

`python3 ~/stratibody_sars-cov-2/makegraph.py y[n°varianti] nomemAb ~/pathSTRATIBODY_WT-mAb.csv ~/pathSTRATIBODY_BETA-mAb.csv ~/pathSTRATIBODY_OMICRON-mAb.csv ~/pathSTRATIBODY_DELTA-mAb.csv ~/pathSTRATIBODY_ALFA-mAb.csv` -> *grafico_RBDvariantsnomemAb*
	
	es : python3 ~/stratibody_sars-cov-2/makegraph.py y5 Bamlanivimab ~/STRATIBODY_WT-LyCov555.csv ~/STRATIBODY_BETA-LyCov555.csv ~/STRATIBODY_OMICRON-LyCov555.csv ~/STRATIBODY_DELTA-LyCov555.csv ~/ALFA-7kmg/STRATIBODY.csv

	if not ALFA : python3 ~/stratibody_sars-cov2/makegraph.py y4 Bamlanivimab ~/STRATIBODY_WT-LyCov555.csv ~/STRATIBODY_BETA-LyCov555.csv ~/STRATIBODY_OMICRON-LyCov555.csv ~/STRATIBODY_DELTA-LyCov555.csv

	ecc ..

Cumulative file 'csv' of the antibody effectiveness against RBD variants:

`python3 ~/stratibody_sars-cov-2/makefile.py nomemAb ~/pathSTRATIBODY_WT-mAb.csv ~/pathSTRATIBODY_ALFA-mAb.csv ~/pathSTRATIBODY_BETA-mAb.csv ~/pathSTRATIBODY_DELTA-mAb.csv ~/pathSTRATIBODY_OMICRON-mAb.csv` -> *STRATIBODY_nomemAB.csv*

To merge all the results:

- find the results in /finalSTRATIBODY/

`python3 ~/stratibody_sars-cov-2/finalSTRATIBODY/finalSTRATIBODY.py STRATIBODY_Bamlanivimab.csv STRATIBODY_Etesevimab.csv STRATIBODY_Regdanvimab.csv STRATIBODY_Cilgavimab.csv STRATIBODY_Tixagevimab.csv STRATIBODY_Sotrovimab.csv STRATIBODY_EY6A.csv`

