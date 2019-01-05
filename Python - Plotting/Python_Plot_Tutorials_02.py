# python tutorial : plotting a graph
# importing packages or module
from numpy import cos, exp, linspace, pi
from matplotlib import pyplot as plt

# define a font properties using dict
font = {'family' : 'serif',
        'color' : 'red',
        'weight' : 'normal',
        'size' : 11
        }

# define x and y axis
x = linspace(0.0, 10.0, 100)
y = cos(2*pi*x)*exp(-x)

# plot
plt.plot(x, y, 'r')
plt.title('Damped exponential decay', fontdict=font)
plt.text(2, 0.65, r'$\cos(2 \pi t) \exp(-t)$', fontdict=font)
plt.xlabel('time (s)', fontdict=font)
plt.ylabel('voltage (mV)', fontdict=font)

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()