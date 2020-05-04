from scipy import signal
import matplotlib.pyplot as plt
from pylab import *

#      Original Signal
s = signal.lti([25], [1, 6, 5, 0])

#     Compensated transfer function
#s = signal.lti([25*0.5, 25], [1*0.0074, 1+6*0.0074, 6+5*0.0074, 5, 0]) 

#     Compensator transfer function
#s = signal.lti([0.5, 1], [0.0074, 1])   


w,mag,phase = signal.bode(s)

subplot(2,1,1)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Magnitude(deg)')
plt.semilogx(w, mag,'b-')
plt.axvline(x = 2.038,ymin=0,color='k',linestyle='dashed')
plt.plot(2.038,0,'o')
plt.grid() 

subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.semilogx(w,phase)   
plt.axvline(x = 2.038,ymin=0,color='k',linestyle='dashed')       # Bode phase plot

plt.axhline(y = -180,xmin=0,color = 'r',linestyle='solid')

plt.grid() 
plt.show()
