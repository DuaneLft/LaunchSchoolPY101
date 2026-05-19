
def compute(integer, operation):

    number_sequence = list(range(1, integer + 1))
    if operation == "+":
        total = 0
        for number in number_sequence:
            total += number
        return total
    elif operation == "*":
        total = 1
        for number in number_sequence:
            total *= number
        return total
    else:
        return None
# These examples should all print True
print(compute(5, '+') == 15)
print(compute(6, '*') == 720)
print(compute(7, '-') == None)