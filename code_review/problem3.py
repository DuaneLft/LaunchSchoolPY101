def multisum(x):
    result = 0
    numbers = list(range(1,x +1))
    for number in numbers:
        if (number % 3 == 0) and (number % 5 == 0):
            result += number
        elif number % 3 == 0:
            result += number
        elif number % 5 == 0:
            result += number
    return result


# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)