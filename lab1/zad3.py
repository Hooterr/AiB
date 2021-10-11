import matplotlib.pyplot as plt
import numpy as np\

def f(x):
	return x*x+5*x
	
x1 = np.arange(-1, 1, 0.1)

plt.figure()
plt.plot(x1, f(x1), 'bo')
plt.show()


x1 = np.arange(-6, 6, 0.1)

plt.figure()
plt.plot(x1, f(x1), 'bo')
plt.show()


x1 = np.arange(0, 5, 0.1)

plt.figure()
plt.plot(x1, f(x1), 'bo')
plt.show()
