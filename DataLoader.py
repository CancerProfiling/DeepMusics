import numpy as np
import pandas as pd
import torch

def sort_data(path):
	
	data = pd.read_csv(path)
	data.sort_values("OS_MONTHS", ascending = False, inplace = True)
	x = data.drop(["SAMPLE_ID", "OS_MONTHS", "OS_EVENT", "Clinical"], axis = 1).values
	ytime = data.loc[:, ["OS_MONTHS"]].values
	yevent = data.loc[:, ["OS_EVENT"]].values
	clinical = data.loc[:, ["Clinical"]].values

	return(x, ytime, yevent,clinical)


def load_data(path, dtype):
	x, ytime, yevent,clinical = sort_data(path)
	X = torch.from_numpy(x).type(dtype)
	YTIME = torch.from_numpy(ytime).type(dtype)
	YEVENT = torch.from_numpy(yevent).type(dtype)
	CLINICAL = torch.from_numpy(clinical).type(dtype)
	if torch.cuda.is_available():
		X = X.cuda()
		YTIME = YTIME.cuda()
		YEVENT = YEVENT.cuda()
		CLINICAL=CLINICAL.cuda()
	return(X, YTIME, YEVENT,CLINICAL)


def load_functional_modules(path, dtype):
	functional_modules_mask = pd.read_csv(path, index_col = 0).as_matrix()
	PATHWAY_MASK = torch.from_numpy(functional_modules_mask).type(dtype)
	if torch.cuda.is_available():
		PATHWAY_MASK = PATHWAY_MASK.cuda()
	return(PATHWAY_MASK)
