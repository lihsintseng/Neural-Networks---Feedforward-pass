# Credit: Li-Hsin Tseng
# https://www.daniweb.com/programming/software-development/threads/39004/what-does-call-method-do

import neural_network
import torch
'''
Part B:
Use the API in NeuralNetwork to create an AND, OR, NOT and XOR networks 
that perform logic operation on boolean values.
logic_gates.py will have four classes as per the second API. 
Each class constructor will call NeuralNetwork class and 
then set the weights of neural network using getLayer([int] layer).
Calling forward function of any logic operation will call forward() 
of NeuralNetwork and return the output of the logic operation.
'''

# Class: [boolean] AND([boolean] x, [boolean] y)
class AND(object):
	def __init__(self):
		self.model = neural_network.NeuralNetwork([2, 1])
		tmp = self.model.getLayer(0)
		tmp[0][0], tmp[1][0], tmp[2][0] = -20, 15, 15 
	def __call__(self, x, y):
		return self.forward(torch.Tensor([x, y]))
	def forward(self, input):
		if self.model.forward(input)[0] >= 0.5:
			return True
		else:
			return False
# Class: [boolean]  OR([boolean] x, [boolean] y)
class OR(object):
	def __init__(self):
		self.model = neural_network.NeuralNetwork([2, 1])
		tmp = self.model.getLayer(0)
		tmp[0][0], tmp[1][0], tmp[2][0] = -5, 15, 15 
	def __call__(self, x, y):
		return self.forward(torch.Tensor([x, y]))
	def forward(self, input):
		if self.model.forward(input)[0] >= 0.5:
			return True
		else:
			return False
# Class: [boolean] NOT([boolean] x)
class NOT(object):
	def __init__(self):
		self.model = neural_network.NeuralNetwork([1, 1])
		tmp = self.model.getLayer(0)
		tmp[0][0], tmp[1][0] = 10, -20 
	def __call__(self, x):
		return self.forward(torch.Tensor([x]))
	def forward(self, input):
		if self.model.forward(input)[0] >= 0.5:
			return True
		else:
			return False
# Class: [boolean] XOR([boolean] x, [boolean] y)
class XOR(object):
	def __init__(self):
		self.model = neural_network.NeuralNetwork([2, 2, 1])
		tmp = self.model.getLayer(0)
		tmp[0][0], tmp[1][0], tmp[2][0] = -150, 300, -300
		tmp[0][1], tmp[1][1], tmp[2][1] = -150, -300, 300
		tmp = self.model.getLayer(1)
		tmp[0][0], tmp[1][0], tmp[2][0] = -100, 100, 100
	def __call__(self, x, y):
		return self.forward(torch.Tensor([x, y]))
	def forward(self, input):
		if self.model.forward(input)[0] >= 0.5:
			return True
		else:
			return False
