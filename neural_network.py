# Credit: Li-Hsin Tseng
import torch
import numpy as np
import math

'''
Part A:
Create a Python script and create an object model of class NeuralNetwork.
Initializing class using __init__(), with the list (in, h1, h2, …, out) as argument, 
will populate the network dictionary with the Θ(layer) matrices 
(which are mapping layer layer to layer + 1), 
initialised to random values (0 mean, 1/sqrt(layer_size) standard deviation). 
The size of the input layer is in, the size of the hidden layers are h1, h2, …, 
and the size of the output layer is out.
getLayer(layer) will return Θ(layer).
By running forward(input) the script will perform the forward propagation 
pass on the network previously built using sigmoid nonlinearities.
'''

'''
def sigmoid(x):
  return 1 / (1 + math.exp(-x))
'''
class NeuralNetwork(object):
	# -- create the dictionary of matrices Θ
	# [nil] __init__(([int] in, [int] h1, [int] h2, …, [int] out))
	def __init__(self, arr):
		self.weights = []
		for i in range(len(arr) - 1):
			tmp = np.random.normal(0, len(arr) ** 0.5, (arr[i]+1) * arr[i+1])
			self.weights.append(tmp.reshape((arr[i+1], arr[i]+1)))

	# -- returns Θ(layer)
	# [2D DoubleTensor] getLayer([int] layer)
	def getLayer(self, layer_num):
		return torch.from_numpy(np.transpose(self.weights[layer_num]))

	# -- feedforward pass single vector
	# [1D DoubleTensor] forward([1D DoubleTensor] input)
	# -- feedforward pass transposed design matrix
	# [2D DoubleTensor] forward([2D DoubleTensor] input)
	def forward(self, input):
		tmp = input.numpy()
		if tmp.ndim == 1:
			tmp = np.transpose([tmp])
		if isinstance(tmp[0], float):
			row_num = 1
		else:
			row_num = len(tmp[0])
		for i in range(len(self.weights)):
			tmp = np.concatenate(([[1.0] * row_num], tmp), axis=0)
			tmp = np.matmul(self.weights[i], tmp)
			for i in range(len(tmp)):
				for j in range(len(tmp[0])):
					sig = 1 / (1 + math.exp(-tmp[i][j]))
					tmp[i][j] = sig
					#tmp[i][j] = 0 if sig < 0.5 else 1
		print(tmp)
		if row_num == 1:
			return torch.squeeze(torch.from_numpy(tmp.T))
		return torch.from_numpy(tmp)
