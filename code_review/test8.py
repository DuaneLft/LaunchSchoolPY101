

def triangle(height):
    line = 1
    while line <= height:
        spaces = ''
        for _ in range(height - line):
            spaces += ' '

        stars = ''
        for _ in range(line):
            stars += '*'

        print(spaces + stars)
        line += 1

triangle(9)
triangle(5)