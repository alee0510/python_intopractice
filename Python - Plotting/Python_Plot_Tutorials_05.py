# physic problem : parabollic motion
# equation : y = v0t-1/2gt^2

# import module
import numpy as np
from matplotlib import pyplot as plt

# font format
font = {'family':'serif',
        'color':'red',
        'weight':'normal',
        'size':11
        }

# initial condition
v0 = 5                              # m/s
g = 9.81                            # m/s2

# define x and y axis
t = np.linspace(0.0, 1.01, 100)     # the value of t (s), linspace(start, stop, n)
y = v0*t - 0.5*g*t**2

# add plot
plt.title(r'parabolic motion', fontdict=font)
plt.xlabel(r'$times (s)$', fontdict=font)
plt.ylabel(r'$velocity (m/s)$', fontdict=font)
plt.plot(t, y, 'r', label=r'$f(x)= vot - 0.5gt^2$')

plt.legend(loc='upper right')       # add a legend

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()