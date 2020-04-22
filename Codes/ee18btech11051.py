import numpy as np
import matplotlib.pyplot as plt

# Different values of w for points
omega = np.append(np.linspace(0,20,100),np.linspace(20,500,100)) 

#Solve the equation into (Magnitude) * exp(Theta)

# This is Theta equation
theta = np.arctan(omega)-np.arctan(omega/10)

# This is the magnitude equation
radius = 10*np.sqrt((1+np.square(omega))/(100+np.square(omega)))

plt.plot(radius*np.cos(theta), radius * np.sin(theta))

ax = plt.subplot(111, projection='polar')
ax.plot(theta, radius)
ax.set_rmax(11)
ax.set_rlabel_position(0)

ax.grid(True)

plt.show()
