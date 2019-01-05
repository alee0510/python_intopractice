# python tutorial : plotting a graph with legend
# importing packages or module
from numpy import cos, sin, exp, linspace, pi
from matplotlib import pyplot as plt

# define a font properties using dict
font = {'family' : 'serif',
        'color' : 'red',
        'weight' : 'normal',
        'size' : 11
        }

# define x and y axis
x = linspace(0, 2*pi, 100)
y = sin(x)
z = cos(x)

# add title
plt.title(r'Graphic sinus & cosinus', fontdict=font)
plt.xlabel(r'$sumbu-x$', fontdict=font)
plt.ylabel(r'$sumbu-y$', fontdict=font)

# plot
plt.plot(x, y, 'r', label=r'$f(x) = \sin(x)$')

#plt.hold(True)
plt.plot(x, z, 'b', label=r'$f(x) = \cos(x)$')
plt.legend(loc='upper right') # add a legend
#plt.hold(False)

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.10)
plt.show()