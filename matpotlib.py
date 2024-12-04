import numpy as np
import matplotlib.pyplot as plt
x1 = np.random.normal(0, 4, 1000)
x2 = np.random.normal(-2, 2, 1000)
x3 = np.random.normal(1, 5, 1000)

kwargs = dict(histtype='stepfilled', alpha = 0.5, density = True, bins = 40)

plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs)

plt.show()
