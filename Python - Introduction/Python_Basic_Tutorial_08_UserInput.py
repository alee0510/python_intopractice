# tutorial 05 : user input
print("Tutorial 08 : User Input\n")

# input, !by default input will be string!
name = input("What is your name? > ")
print("Hello {}!".format(name))

print("\n")
number = input("Please enter a number > ")
print("Your number is {}".format(number))
print(number + number)                      # the output will be "1010", str+str

# convert input to float or integer
print("\nafter convert the input number")
x = float(number)
print(x)
print(x+x)                                  # the output will be "a number not string"