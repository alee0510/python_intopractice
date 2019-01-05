# tutorial 04 : loop
print("Tutorial 04 : Loop\n")

# for loop
# integer loop
print("loop from 0 to 10")          # note : python start index by 0 not 1
for x in range(0, 10):              # 10 will not be show up
    print(x)

print("\nloop by 2 step")
for x in range(0, 10, 2):
    print(x)

print("\nloop backward")
for x in range(10, 0, -1):          # 0 will not be show up
    print(x)

# string loop
print("\nsting loop")
title = "tutorial string loop"
for index in range(0, len(title)):
    print(title[index])

print("\nstring loop with step by 2")
for index in range(0, len(title), 2):
    print(title[index])

print("\nstring lopp bacward")
for index in range(len(title)-1, -1, -1):
    print(title[index])
# special methods
print("\nspecial methods")
for letter in title:
    print(letter)

# while loop, its an infinite loop, it will be loop forever while the value is True
# this function is used for game development that required the program running forever
# until system break it (with a special condition)
print("\nwhile loop")
y = 5
while y < 11:   # 11 will not be show up
    print(y)
    y = y + 1   # or it can be written by y += 1, increment

# backward
y = 9
while y > 0:    # 9 will be show up
    print(y)
    y = y - 1   # or it can be written by y -= 1, decrement