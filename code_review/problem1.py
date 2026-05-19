def is_leap_year(year):
    is_a_leap_year = False
    if year % 400 == 0:
        is_a_leap_year = True
    if (year % 4 == 0) and (year % 100 != 0):
        is_a_leap_year = True
    return is_a_leap_year

# These examples should all print True
print(is_leap_year(1) is False)
print(is_leap_year(2) is False)
print(is_leap_year(3) is False)
print(is_leap_year(4) is True)
print(is_leap_year(1000) is False)
print(is_leap_year(1100) is False)
print(is_leap_year(1200) is True)
print(is_leap_year(1300) is False)
print(is_leap_year(1751) is False)
print(is_leap_year(1752) is True)
print(is_leap_year(1753) is False)
print(is_leap_year(1800) is False)
print(is_leap_year(1900) is False)
print(is_leap_year(2000) is True)
print(is_leap_year(2023) is False)
print(is_leap_year(2024) is True)
print(is_leap_year(2025) is False)