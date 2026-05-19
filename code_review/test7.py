
def crunch(text):
    result = ''
    i = 0
    while i < len(text):
       # if i < len(text) - 1:
        if text[i] != text[i + 1]:
            result += text[i]
        else:
            result += text[i]
        i += 1
    return result





# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')