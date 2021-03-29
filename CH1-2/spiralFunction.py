from nnfs.datasets import spiral_data
import matplotlib.pyplot as plt

X, y = spiral_data(samples=100, classes=3)
# plt.scatter(X[:,0], X[:,1])
# plt.show()

plt.scatter(X[:, 0], X[:, 1], c=y, cmap='brg')
plt.show()
