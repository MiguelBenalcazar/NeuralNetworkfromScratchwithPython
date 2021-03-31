#define a list of inputs
inputs = [0, 2, -1, 3.3, -2.7, 1.1, 2.2, -100]
#define a list to keep the outputs
output = []

for i in inputs:
    if i > 0:
        output.append(i)
    else:
        output.append(0)

print(output)

del output[:] #clear list

for i in inputs:
    output.append(max(0, i))  #max return max item between 0 and i

print(output)

del output[:]

#Using numpy
import numpy as np
output = np.maximum(0, inputs)
print(output)
