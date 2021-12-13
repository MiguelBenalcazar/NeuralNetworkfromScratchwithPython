import numpy as np

# Define inputs
inputs = [1, 2, 3, 2.5]
# Define weights
weights = [[0.2, 0.8, -0.5, 1],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]
# Define biases of the three neurons
biases = [2, 3, 0.5]

outputs = np.dot(weights, inputs) + biases

print(outputs)
