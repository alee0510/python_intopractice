# python tutorial 03 : conditional
print("Tutorial 03 : Conditional\n")

# conditional if function
print("if function")
print("3 is equal 3?")
if 3 == 3: # == mean equal
    print(True)

# comparison integer
# == equal, > greater than, < less than, >= greater equal, <= less equal
x = 3
y = 5
print("\n{} is greater than {} ?".format(x,y))
if x > y: 
    print(True)
else:
    print(False)

print("\n{} is less than {} ?".format(x,y))
if x < y:
    print(True)
else:
    print(False)

# string comparison
# comparison value, 1 true and 0 false
# 1 and 1 = 1  1 and 0 = 0    0 and 1 = 0
# 1 or 1 = 1   1 or 0 = 1     0 or 1 = 1     0 or 0 = 0
# not 1 = 0    not 0 = 1
print("\nRock Scissor and Paper Game")
player_a = "rock"
player_b = "scissor"
if player_a == "rock" or player_b == "rock":        # true or false = true
    print("someone choose rock")

if player_a == "rock" and player_b == "scissor":    # true and true = true
    print("Player A WIN!")
elif player_a == "rock" and player_b == "papper":   # true and false = false
    print("Player B WIN!")
else:
    print("Tie!")