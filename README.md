## Systematic characterization of multi-comics landscape between gut microbial metabolites and GPCRome. Yunguang Qiu, et al.

Instructions:

ML_code directory for ML models generation and prediction:


	1. The features were calculated by using deltaVinaXGB (https://github.com/jenniening/deltaVinaXGB).

	2. The mechine learning model were created and evaluated by using open-source Pycaret 2.2 [full version].

	3. The process of creating ML models can be found in ml.ipynb.
 
 	4. The et_model.tar.gz is pre-trained extra trees model, which could be called directly in ml.ipynb.

  	5. The GNN model is built separately (GNN_model.tar.gz). 


References:
1. Lu J, et al., Incorporating Explicit Water Molecules and Ligand Conformation Stability in Machine-Learning Scoring Functions. Journal of Chemical Information and Modeling 59, 4540-4549 (2019).
2. pycaret.org. PyCaret, April 2020. URL https://pycaret.org/about. PyCaret version 1.0.0.
3. https://github.com/HyunSeobKim/CHEM-BERT


Pocket_classfication_code directory for scripts of identifing and matching pocket position in GPCR receptor:

	1. match generic numbers to sequence numbers for each model file: (e.g., all ClassA GPCR generic numbers)

	model_residue_match.py

	2. for each pocket file, judge whether pocket belong to orthersteric pocket: (mathch the intersection of sequence number of pocekt with pocket sequence number; e.g., classA: resi >=5)

	pocket_generic_numer_match_resi5.py

	3. for each docking result, match docking pocket to above analyzed type of pocket; (for each docking results file)

	match_gpcruniq_file.py

