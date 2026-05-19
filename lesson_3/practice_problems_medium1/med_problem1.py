# For this practice problem, write a program that outputs The Flintstones Rock!
# 10 times, with each line prefixed by one more hyphen than the line above it.
# The output should start out like this:
# -The Flintstones Rock!
# --The Flintstones Rock!
#     ...

message = 'The Flintstones Rock!'
HYPHEN = '-'
i = 0
while i < 10:
    message = f"{HYPHEN}{message}"
    print(message)
    i += 1

for padding in range(1,11):
    print(f'{"-" * padding} The Flintstones Rock!')
