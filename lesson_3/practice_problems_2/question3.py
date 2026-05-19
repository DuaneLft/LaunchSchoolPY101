# Programmatically determine whether 42 lies between 10 and 100, inclusive.
# Do the same for the values 100 and 101

num1 = 42
num2 = 100
num3 = 101
ten_to_hundred = list(range(10, 101))

print(num1 in ten_to_hundred)
print(num2 in ten_to_hundred)
print(num3 in ten_to_hundred)