# Write two distinct ways of reversing the list without mutating the original list.

numbers = [1, 2, 3, 4, 5]

reversed_1 = list(reversed(numbers))
reversed_2 = numbers[::-1]
print(reversed_1)
print(reversed_2)

numbers.reverse()
print(numbers)

# The reverse method mutates the existing list and returns None so you must 
# use the original variable.