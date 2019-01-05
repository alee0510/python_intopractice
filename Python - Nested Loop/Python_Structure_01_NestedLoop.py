# python tutorial : nested loop
print("Tutorial Python Structure : Nested Loop!\n")

# basic for loop
print("basic for loop")
for x in range(0, 10):
    print(x, end=" ")                   # end=" " is to make output vertical

print()
# structure nested loop
print("\nstructure nested loop")
maxRaw = int(input("Enter number of raw > "))
n = 1
for raw in range(1, maxRaw+1):          # ex : raw 4, because python start index from 0, so 0+1 =1, maxRaw+1 
    for column in range(1, raw+1):      # column = raw, 0+1=1, raw+1
        print(n, end=" ")
        n += 1
    print()                             # to print in next raw

print()
# nested loop star
print("nested loop star")
for raw in range(1, maxRaw+1):
    for column in range(1, raw+1):
        print("*", end=" ")
    print()

print()
# nested loop double variable
print("nested loop double variable")
for i in range(1, maxRaw+1):
    for j in range(1, i+1):
        if j == i:
            print("x", end=" ")
        else:
            print("*", end=" ")
    print()