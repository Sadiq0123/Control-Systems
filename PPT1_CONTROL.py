import numpy as np
import matplotlib.pyplot as plt

omega = np.append(np.linspace(0,20,100),np.linspace(20,500,100))
theta = np.arctan(omega)-np.arctan(omega/10)
radius = 10*np.sqrt((1+np.square(omega))/(100+np.square(omega)))

plt.plot(radius*np.cos(theta), radius * np.sin(theta))
plt.xlim([-2,12])
plt.ylim([-2,8])
plt.axhline(0, color = 'black')
plt.axvline(0, color = 'black')
plt.grid()
plt.show()
