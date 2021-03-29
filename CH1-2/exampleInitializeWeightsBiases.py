import numpy as np
import nnfs

nnfs.init()

# define number of inputs
n_inputs = 2
# define number of neurons
n_neurons = 4

weights = 0.01 * np.random.randn(n_inputs, n_neurons)
biases = np.zeros((1, n_neurons))

print(weights)
print(biases)
