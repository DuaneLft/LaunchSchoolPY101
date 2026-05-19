# Alan wrote the following function, which was intended to return all of the
# factors of number: Alyssa noticed that this code would fail when the input is
# a negative number, and asked Alan to change the loop. How can he make this
# work? Note that we're not looking to find the factors for negative numbers,
# but we want to handle it gracefully instead of going into an infinite loop.
# Bonus Question: What is the purpose of number % divisor == 0 in that code?
# Bonus Answer: The purpose is to test wether or not number is evenly divided
# by the divisor, if so the divisor is a factor of the number.

def factors(number):
    divisor = number
    result = []
    if number == 0:
        return "The only divisor of 0 is 0"
    if number < 0:
        number *= -1
        divisor = number
        print(
            'This tool does not give factor of negative numbers. Your number '
            'has been converted to a positive.'
            )
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result
print(factors(-576))