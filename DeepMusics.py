import torch
import torch.nn as nn

class DeepMusicsNet(nn.Module):
	def __init__(self, In_Nodes, functional_Nodes, Hidden_Nodes,Out_Nodes, functional_Mask):
		super(DeepMusicsNet, self).__init__()
		self.tanh = nn.Tanh()
		self.pathway_mask = functional_Mask
		self.sc1 = nn.Linear(In_Nodes, functional_Nodes)
		self.sc2 = nn.Linear(functional_Nodes, Hidden_Nodes)
		self.sc3 = nn.Linear(Hidden_Nodes, Out_Nodes, bias=False)
		self.sc4 = nn.Linear(Out_Nodes+1,1, bias = False)
		self.sc4.weight.data.uniform_(-0.001, 0.001)
		self.do_m1 = torch.ones(functional_Nodes)
		self.do_m2 = torch.ones(Hidden_Nodes)
		if torch.cuda.is_available():
			self.do_m1 = self.do_m1.cuda()
			self.do_m2 = self.do_m2.cuda()
		###

	def forward(self, x_1, x_2):
		self.sc1.weight.data = self.sc1.weight.data.mul(self.pathway_mask)
		x_1 = self.tanh(self.sc1(x_1))
		if self.training == True: 
			x_1 = x_1.mul(self.do_m1)
		x_1 = self.tanh(self.sc2(x_1))
		if self.training == True:
			x_1 = x_1.mul(self.do_m2)
		x_1 = self.tanh(self.sc3(x_1))
		x_cat = torch.cat((x_1, x_2), 1)
		lin_pred = self.sc4(x_cat)
		
		return lin_pred

