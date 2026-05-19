def center_of(string):
  l = len(string)
  if l%2==0:
      middle_chars = string[(l/2) - 1] + string[l/2]
      return middle_chars
  else:
    return string[l//2]
# These examples should all print True
print(center_of('I love Python!!!') == "Py")
print(center_of('Launch School') == " ")
print(center_of('Launchschool') == "hs")
print(center_of('Launch') == "un")
print(center_of('Launch School is #1') == "h")
print(center_of('x') == "x")