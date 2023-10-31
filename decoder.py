password = input()
result = ''
# initializes the return variable
for digit in password:
    character = int(digit) - 3
    if character < 0:
        # changes negative integers into their positive counterparts
        character = str(character + 10)
    result += str(character)

print(result)