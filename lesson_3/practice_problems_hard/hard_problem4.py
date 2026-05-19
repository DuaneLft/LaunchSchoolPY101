# Ben was tasked to write a simple Python function to determine whether an
# input string is an IP address using 4 dot-separated numbers, e.g., 10.4.5.11.
# Alyssa supplied Ben with aa function named is_an_ip_number . It determines
# whether a string is a numeric string between 0 and 255 as required for IP
# numbers and asked Ben to use it. Here's the code Ben wrote:
#
# Alyssa reviewed Ben's code and said, It's a good start, but you missed a few
# things. You're not returning a false condition, and you're not handling the
# case when the input string has more or less than 4 components. e.g., 4.5.5 or
# 1.2.3.4.5 :    Fix the code



def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False
    return True

def is_an_ip_number(num_str):
    if num_str.isdigit():
        number = int(num_str)
        return 0 <= number <= 255
    return False

print(is_dot_separated_ip_address("12.233.45.33"))
print(is_dot_separated_ip_address("234.345.21.22"))
print(is_dot_separated_ip_address("233.11.14.25.78"))