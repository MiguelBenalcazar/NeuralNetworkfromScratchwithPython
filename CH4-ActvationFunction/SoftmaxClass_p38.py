import numpy as np

# Softmax activation
class Activation_Softmax:

    # Forward pass
    def forward(self, inputs):
        # Get unnormalized probabilities
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))

        # Normalize them for each sample
        probabilities = exp_values / np.sum(exp_values, axis=1,keepdims=True)
        self.output = probabilities


x = [[1, 2, 3]]
softmax = Activation_Softmax()
softmax.forward(x)
out_x = softmax.output
print( "softmax({}) = {}".format(x,out_x))

y = [[-2, -1, 0]]
softmax.forward(y)
out_y  = softmax.output
print( "softmax({}) = {}".format(y,out_y))

z = np.divide(x,2)
softmax.forward(z)
out_z = softmax.output
print( "softmax({}) = {}".format(z,out_z))

