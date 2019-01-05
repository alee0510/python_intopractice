# tutorial 06 : dictionaries
print("Tutorial 06 : Dictionaries\n")

# create a dictionaries {}
capitals = {"Japan":"Tokyo", "Korea":"Seoul"} # format in dictionaries {"Key": "Value"}

print(capitals)
print(len(capitals))

# define a variable that contain a key in dictionaries
capital = capitals["Korea"]
print(capital)

# add new key in a dictionaries
capitals["China"]="Beijing"
print("\nnew dictionaries")
print(capitals)

# spit out the dictionaries
print("\nspit out the dictionarise")
for x in capitals:
    print(x, capitals[x])
# NOTE, in dictionaries, it will only print out the key.
# to get the value, you must use the key in brackets []
# following the dictionary's name

# define a value
print("\nloop function")
for country in capitals:
    capital = capitals[country]
    print("The Capital of {} is {}.".format(country, capital))