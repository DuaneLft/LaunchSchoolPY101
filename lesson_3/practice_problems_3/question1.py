# Write two different ways to remove all of the elements from the following 
# list:

numbers = [1, 2, 3, 4]

numbers.clear()

# Also 
# While numbers:
#     numbers.pop()

# Note that the following solution will set numbers to an empty list, but 
# doesn't clear the original list (It could still be in memory). That's fine if you know there are no other 
# refrences to the list. 
# numbers = []