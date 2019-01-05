# python tutorial : plotting a graph from a file
# importing packages or module
from numpy import cos, sin, exp, linspace, pi
from matplotlib import pyplot as plt
from pylab import genfromtxt, plot

# define a font properties using dict
font = {'family' : 'serif',
        'color' : 'red',
        'weight' : 'normal',
        'size' : 11
        }

# importing data from a file
data = genfromtxt('data_plot.txt')

# separating data [raw : column]
mass = data[:, 0]
radius = data[:, 1]
print(mass)

# plot data
plot(mass, radius, 'r', label=r'data plot')

# add title and axis's label
plt.title(r'Contoh Relasi Masa dan Radius Bintang', fontdict=font)
plt.xlabel(r'$M {\odot}$', fontdict=font)
plt.ylabel(r'$M {\odot}$', fontdict=font)

plt.legend(loc='upper right')  # add a legend

plt.grid(True) # start to grid a plot

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.10)
plt.show()