# python tutorial 01 : Basic Command

# print command
print("Tutorial 01 : Print Command")
print("Hello World!")
print("Hello"+" "+"World!")             # its basicly do same command

# string Variable
name = "Ali Muksin"                     # define a string variable called name
print("\n")                             # created new line
print(name)
print(len(name))                        # len=how many characters in the string variable

print("\n")
print("My Name is: "+name)
print("My Name is: %s" %name)           # %s mean to make any data to string type
print("My Name is: {}".format(name))    # replace in {} with variable format

# string methods
print("\nString Methods")
print("Hello".upper())
print("hELOo".lower()+"\n")

title = "Tutorial pyThon basic command"
print(title.capitalize())
print(title.title())                    # title() is a string methods

print("\nSlice")
print("Hello World!"[0:4])              # python index start with 0 not 1
print("Hello World!"[:7])               # it will assume start 0 to 7
print(title[:5])
print(title[2:])