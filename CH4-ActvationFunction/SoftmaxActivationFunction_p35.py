import numpy as np

# Values from the earlier previous when we described
# what a neural network is

layer_outputs = [4.8, 1.21, 2.385]

# For each value in a vector, calculate the exponential value
exp_values = np.exp(layer_outputs)
print("exponentiated values: {}".format(exp_values))

# Now normalize values
norm_values = exp_values / np.sum(exp_values)

print('normalized exponentiated values: {}'.format(norm_values))
print('sum of normalized values: {}'.format(np.sum(norm_values)))
