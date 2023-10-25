while True:
    password = input()
    result = ''
    for digit in password:
        character = int(digit) - 3
        if character < 0:
            character = str(character + 10)
        result += str(character)

    print(result)