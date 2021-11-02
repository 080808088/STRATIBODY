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
- **_7C01_** -> *Ly-cov016 (CB6)*

- **_7KMG_** -> *Ly-Cov555*

- **_7L7D_** -> *AZD8895*

- **_7L7E_** -> *AZD1061*

- **_6ZCZ_** -> *EY6A*

- **_6XE1_** -> *CV30*

Variants Sars-Cov-2 monitored by WHO [World Health Organization](https://www.who.int/en/activities/tracking-SARS-CoV-2-variants/)

~script in progress~

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

- **6XE1** :

	 	- chain E Spike-RBD -> chain A

		- chain H Heavy Fab -> chain B

		- chain L Light Fab -> chain C
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

`python3 ~/htmd/protein.py -s ~/path_to/pdbPREP.pdb -nt 16 -ns 100 -ff oplsaa -d 1 -bt dodecahedron -ntmpi -trj`

If mutation **Docking** or: [script checking variants in progress ..] 

-r; -a : `python3 ~/htmd/protein.py -s ~/pdbPREP.pdb -nt 1 -ns 100 –ff oplsaa -d 1 -bt dodecahedron -r "A-417,A-452,A-478" -a "THR,ARG,LYS" -ntmpi -trj`

For further information `python3 ~/htmd/protein.py -h`

### 6. Molecular Dynamic Analysis
`python3 ~/htmd/native.py -tpr MD.tpr -xtc trj.xtc -method switch_function -sel_A "segid A" -sel_B "segid B"` -> *segid B_with_segid A.pkl*; *contacts_of_segid B_with_segid A.png*

`python3 ~/htmd/native.py -tpr MD.tpr -xtc trj.xtc -method switch_function -sel_A "segid A" -sel_B "segid C"` -> *segid C_with_segid A.pkl*; *contacts_of_segid C_with_segid A.png*
### 7. Data Analysis
`python3 stratibody_sars-cov-2/analysisMD.py segid\ B_with_segid\ A.pkl segid\ C_with_segid\ A.pkl RBDtype mAbname` -> *STRATIBODY.csv*
