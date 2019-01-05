# python tutorial : pyramid
print("Tutorial Python Structure : Pyramid!\n")

print("star pyramid")
maxRaw = int(input("Enter a number of raw > "))
for raw in range(0, maxRaw):
    for column in range(0, maxRaw-raw-1): # printed space
        print(end=" ")
    for column in range(0, raw+1): # printed *
        print("*", end=" ")
    print()

# pyramid with a number
print()
print("number pyramid")
x = 1
for raw in range(0, maxRaw):
    for column in range(0, maxRaw-raw-1):
        print(end=" ")
    for column in range(0, raw+1):
        print(x, end=" ")
        x += 1
    print()
    #x = 1