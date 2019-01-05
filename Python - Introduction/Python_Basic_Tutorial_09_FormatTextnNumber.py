# tutorial 09 : text and number formating
print("Tutorial 09 : Text and Number Formating\n")

# before formating
print("EX 01 : Before formating")
real = 12.456789
integer = 45
string = 'string'
print("real={} integer={} string={}".format(real, integer, string))

# after formating
print("\nafter formating")
print ("real=%.3f, integer=%d, string=%s" %(real, integer, string))
print("real=%9.3e, integer=%5d, string=%s" %(real, integer, string))
# %.f(real number, %.d(integer), %s(string)
# %9.3f, 3 mean the number after ., ex : 12.45, 9 mean max character
# e or E mean the result will in scientific notation, ex : 1.290e+01 or 1.290E+0
# %5d means that an integer is to bewritten in a ﬁeld of width equal to 5 characters
# real number also specified by %g

# next example
print("\nEX 02 : Print Formating")
from math import sin

t0 = 2
dt = 0.5

# unformated print
print("unformated print")

t1 = t0 + 0*dt; g1 = t1*sin(t1)
print(t1, g1)

t2 = t0 + 1*dt; g2 = t2*sin(t2)
print(t2, g2)

t3 = t0 + 2*dt; g3 = t3*sin(t3)
print(t3, g3)

# formated print
print("\nafter formating")
print("%6.2f %8.3f" %(t1, g1))
print("%6.2f %8.3f" %(t2, g2))
print("%6.2f %8.3f" %(t3, g3))

# modern syntax
print("\nmodern syntax")
print("{:.2f} {:.3f}".format(t1, g1))
print("{:.2f} {:.3f}".format(t2, g2))
print("{:.2f} {:.3f}".format(t3, g3))