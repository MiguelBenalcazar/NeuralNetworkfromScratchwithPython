import numpy as np
softmax_outputs = [[0.7, 0.1, 0.2],
                   [0.1, 0.5, 0.4],
                   [0.02, 0.9, 0.08]]
class_targets = [0, 1, 1] #dog, cat, cat

for targ_idx, distribution in zip(class_targets, softmax_outputs):
    print('targets {}, softmax_outputs {}, prediction {} '.format(targ_idx, distribution, distribution[targ_idx]))


softmax_outputs = np.array([[0.7, 0.1, 0.2],
                   [0.1, 0.5, 0.4],
                   [0.02, 0.9, 0.08]])

class_targets = [0, 1, 1] #dog, cat, cat

print(softmax_outputs[[0, 1, 2], class_targets])

print(softmax_outputs[range(len(softmax_outputs)), class_targets])

print(-np.log(softmax_outputs[range(len(softmax_outputs)), class_targets]))

neg_log = -np.log(softmax_outputs[range(len(softmax_outputs)), class_targets])

average_loss = np.mean(neg_log)
print(average_loss)