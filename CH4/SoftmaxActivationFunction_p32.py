import math

# values from the previous output when we describe
# what a neural network is
layer_outputs = [4.8, 1.21, 2.385]

# e - mathematical constant, we use E here to match a common coding
# style where constants are upercase

E = math.e

# for each value in a vector, calculate the exponential value
exp_values = []
for output in layer_outputs:
    exp_values.append(E ** output) # ** - power operator in Python

print('exponentiated values: {}'.format(exp_values))


#normalize values
norm_base = sum(exp_values)
norm_values = []

for value in exp_values:
    norm_values.append(value / norm_base)

print('Normalized exponentiated values:')
print(norm_values)

print('Sum of normalized values: {}'.format(sum(norm_values)))