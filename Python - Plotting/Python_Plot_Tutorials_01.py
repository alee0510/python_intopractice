# python tutorial : plotting a graph
# numpy is powerful numeric module in python
# matplotlib is use to plot a graphic

# importing packages or module
import numpy as np
import matplotlib.pyplot as plt

# define x and y axis
x = np.linspace(0, 2*np.pi, 100)
y = np.cos(x)                       # f(x) = cos(x)

# add title
plt.title("Graphic of Sinus")
plt.xlabel("x")
plt.ylabel("y")

# plot a graph
plt.plot(x, y)
plt.show()                          # show the graph