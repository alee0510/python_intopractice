# tutorial 05 : list
print("Tutorial 05 : List\n")

# List Methods []
# .append(value), appends element to end of the list
# .count('x'), counts the number of occurrences of 'x' in the list
# .index('x'), returns the index of 'x' in the list
# .insert('y','x'), inserts 'x' at location 'y'
# .pop(), returns last element then removes it from the list
# .remove('x'), finds and removes first 'x' from list
# .reverse(), reverses the elements in the list
# .sort(), sorts the list alphabetically in ascending order,
#  or numerical in ascending order

# make a list
names = ["Ali", "Irham", "Uci", "Chan"]
print("name in the list : ", names)
print("lenght of the list : ", len(names))

names.append("Fitri")       # add new member to the list, at the end
print("\nnew list : ", names)

# slice
print("\nslice")
print(names[1])             # output Irham, index start by 0
print(names[0:4])           # output Ali, Irham, Uci, Chan

# for function
print("\nfor function")
for index in range(0, len(names)):
    print(names[index])

# special methods
print("\nspecial method")
for name in names:
    print(name)

# using methods
print("\nsorting a list")
names.sort()
print(names)
for name in names:
    print(name)

# integer list
print("\ninteger list")
scores = [0, 5, 6, 21, 9, 11, 67, 34, 12, 8]
scores.sort()
print(scores)
for score in scores:
    print(score)