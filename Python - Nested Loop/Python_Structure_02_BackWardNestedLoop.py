# python tutorial : backward nested loop
print("Tutorial Python Structure : Backward Nested Loop!\n")

maxRaw = int(input("Enter a number of raw > "))
n = 1
for raw in range(maxRaw, 0, -1):
    for column in range(raw, 0, -1):
        print(n, end=" ")
        n += 1
    print()
    n = 1 # refresh n to 1 again

print()
# backward nested loop, star
for raw in range(maxRaw, 0, -1):
    for column in range(raw, 0, -1):
        print("*", end=" ")
    print()

print()
# bacward nested loop 03
x = maxRaw
for raw in range(maxRaw, 0, -1):
    for column in range(raw, 0, -1):
        print(maxRaw, end=" ")
        maxRaw -= 1
    print()
    maxRaw = x # refresh the value of maxRaw