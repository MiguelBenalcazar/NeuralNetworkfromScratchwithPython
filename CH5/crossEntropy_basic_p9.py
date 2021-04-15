import math

# An example output from the outpur layer of the neural network
# y_hat
# softmax_output =  [0.7, 0.1, 0.2]
softmax_output = [0.4, 0.2, 0.4]
#Ground truth --> Target --> y
target_output = [1, 0, 0]
loss = - (math.log(softmax_output[0]) * target_output[0] +
          math.log(softmax_output[1]) * target_output[1] +
          math.log(softmax_output[2]) * target_output[2])
print("the confidence level of the first class is:  {}".format(loss))