str1 = "Come over here!"
str2 = "What's up Doc?"
print(str1.endswith("!"))
print(str2.endswith("!"))


def string_ending(value):
    str_to_list = list(value)
    if str_to_list[-1] == "!":
        return True
    return False

print(string_ending(str1))
print(string_ending(str2))