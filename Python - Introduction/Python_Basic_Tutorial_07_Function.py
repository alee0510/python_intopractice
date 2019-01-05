# tutorial 07 : function
print("Tutorial 07 : Function\n")

# function without return value
print("function without return value")
def print_pi():                         # define a function, without parameter
    print("3.14159")
print_pi()                              # calling a function

def print_double(x):                    # function with parameter
    print(x*2)
print_double(4)

# function with return value
print("\nfunction with return value")

def get_pi():
    return 3.14159
x = get_pi()                            # define a variable x with value from a function
print(x)

def get_double(x):
    return x*2
x = get_double(9)
print(x)

# nested function
print("nested function")
def get_greatest(x, y):
    if x > y:
        return x
    else:
        return y

greatest = get_greatest(55, 79)
print(greatest)

# odd or even function
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

if is_even(100) is True:
    print("Event!")
else:
    print("Odd!")

# function with 2 retun value
def xy(v0x, v0y, t): # we also can make an initial value direct on def xy(t, v0x=0, v0y=0):
    g = 9.81 # acceleration of gravity 
    return v0x*t, v0y*t - 0.5*g*t**2

print(xy(10, 15, 5))

# or
vx, vy = xy(10, 15, 5)
print(vx, vy)