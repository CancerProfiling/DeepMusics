from DataLoader import load_data, load_pathway
from train import trainDeepMusicsNet
import torch
import numpy as np
torch.cuda.set_device(9)
dtype = torch.FloatTensor
In_Nodes = 11048
Pathway_Nodes = 860 
Hidden_Nodes = 100 
Out_Nodes = 30
Initial_Learning_Rate = [0.003, 0.001, 0.0001, 0.000075]
L2_Lambda = [0.1, 0.01, 0.005, 0.001]
num_epochs = 3000 
Num_EPOCHS = 20000 
Dropout_Rate = [0.7, 0.5]

pathway_mask = load_pathway("~/pathway_mask_scna_rna.csv", dtype)
x_train, ytime_train, yevent_train, clinical_train = load_data("~/scna_rna.train.csv", dtype)
x_valid, ytime_valid, yevent_valid, clinical_valid = load_data("~/scna_rna.test.csv", dtype)
x_test, ytime_test, yevent_test, clinical_test = load_data("~/scna_rna.validation.csv", dtype)

opt_l2_loss = 0
opt_lr_loss = 0
opt_loss = torch.Tensor([float("Inf")])
###if gpu is being used
if torch.cuda.is_available():
	opt_loss = opt_loss.cuda()
###
opt_c_index_va = 0
opt_c_index_tr = 0
for l2 in L2_Lambda:
	for lr in Initial_Learning_Rate:
		loss_train, loss_valid, c_index_tr, c_index_va = trainDeepMusicsNet(x_train, clinical_train, ytime_train, yevent_train, \
																x_valid, clinical_valid, ytime_valid, yevent_valid, pathway_mask, \
																In_Nodes, Pathway_Nodes, Hidden_Nodes, Out_Nodes, \
																lr, l2, num_epochs, Dropout_Rate)
		if loss_valid < opt_loss:
			opt_l2_loss = l2
			opt_lr_loss = lr
			opt_loss = loss_valid
			opt_c_index_tr = c_index_tr
			opt_c_index_va = c_index_va
		print ("L2: ", l2, "LR: ", lr, "Loss in Validation: ", loss_valid)
