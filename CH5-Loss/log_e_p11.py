import numpy as np
import matplotlib.pyplot as plt
b = 5.2
r = np.log(b)
print(r)



import math
print(math.e ** r)

x = np.linspace(1, 100, num=100)
y = [np.log(xx) for xx in x]

x1 = np.linspace(1, 100, num=100)
y1 = [math.e ** (xx) for xx in x1]

plt.figure(2)
plt.subplot(211)
plt.plot(x, y, linewidth = 2.0)
plt.subplot(212)
plt.plot(x1, y1, linewidth = 2.0)
plt.show()


