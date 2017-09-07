### Neural Networks - Feedforward pass
##### Author: Li-Hsin Tseng
Source code: neural_network.py, logic_gates.py, test.py 

##### neural_network.py

In <b>neural_network.py</b> is the class <b>NeuralNetwork</b>. With the init function, it initializes the weights in the network with the specify number of nodes in each layer. The initial weights in each layer are in random <br>
With the <b>getLayer</b> function, one can get the weights in between layers.
As for the <b>forward</b> function, it did the multiplication with the weights and input layer by layer. After the matrix multiplication, the values go through the sigmoid function and head to the next layer.
<br><br>

##### logic_gates.py

In <b>logic_gates.py</b> are four classes including the AND, OR, NOT, and XOR gates with the help of neural_network.py. After initializing them with the right weights in the layers. One can use it to produce the results of gate operations.

* AND

<b>coefficients: [-20, 15, 15 ]<br></b>
AND(True, True) = True<br>
AND(True, False) = False<br>
AND(False, True) = False<br>
AND(False, False) = False<br>
* OR

<b>coefficients: [-5, 15, 15 ]<br></b>
OR(True, True) = True<br>
OR(True, False) = True<br>
OR(False, True) = True<br>
OR(False, False) = False<br>

* NOT

<b>coefficients: [10, -20 ]<br></b>
NOT(True) = False<br>
NOT(False) = True<br>
* XOR

XOR definition: <br>
<b>A XOR B = ( A & ( -B ) ) + ( ( -A ) & B ) <br></b>

<b>coefficients: <br>
layer 0 : [[-15, 20, -20], [-15, -20, 20]] <br>
layer 1 : [-10, 10, 10] <br></b>
XOR(True, True) = False<br>
XOR(True, False) = True<br>
XOR(False, True) = True<br>
XOR(False, False) = False<br>

