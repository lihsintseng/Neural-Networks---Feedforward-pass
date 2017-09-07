# Credit: Li-Hsin Tseng
import logic_gates
import torch
import neural_network

model = neural_network.NeuralNetwork([2, 2, 1])
x, y, z = 1, 2, 3
res = model.forward(torch.Tensor([[x, y, z], [x, y, z]]))
print(res)


AND = logic_gates.AND()
NOT = logic_gates.NOT()
OR = logic_gates.OR()
XOR = logic_gates.XOR()
'''
print('AND')
print(AND(True, True)) 
print(AND(True, False))
print(AND(False, True))
print(AND(False, False))

print('NOR')
print(NOT(True))
print(NOT(False))

print('OR')
print(OR(True, True))
print(OR(True, False))
print(OR(False, True))
print(OR(False, False))
'''
print('XOR')
print(XOR(True, True))
print(XOR(True, False))
print(XOR(False, True))
print(XOR(False, False))
