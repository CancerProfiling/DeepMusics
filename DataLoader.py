import numpy as np
import pandas as pd
import torch

def sort_data(path):
	
	data = pd.read_csv(path)
	data.sort_values("OS_MONTHS", ascending = False, inplace = True)
	x = data.drop(["SAMPLE_ID", "OS_MONTHS", "OS_EVENT"], axis = 1).values
	ytime = data.loc[:, ["OS_MONTHS"]].values
	yevent = data.loc[:, ["OS_EVENT"]].values
	return(x, ytime, yevent)


def load_data(path, dtype):
	x, ytime, yevent = sort_data(path)

	X = torch.from_numpy(x).type(dtype)
	YTIME = torch.from_numpy(ytime).type(dtype)
	YEVENT = torch.from_numpy(yevent).type(dtype)
	if torch.cuda.is_available():
		X = X.cuda()
		YTIME = YTIME.cuda()
		YEVENT = YEVENT.cuda()
	return(X, YTIME, YEVENT)


def load_pathway(path, dtype):
	pathway_mask = pd.read_csv(path, index_col = 0).as_matrix()
	PATHWAY_MASK = torch.from_numpy(pathway_mask).type(dtype)
	if torch.cuda.is_available():
		PATHWAY_MASK = PATHWAY_MASK.cuda()
	return(PATHWAY_MASK)