def encode(password):
    result = ''
    for digit in password:
        character = str(int(digit) + 3)
        if int(character) >= 10:
            character = int(character)-10
            character = str()
        result += character

    return result


def decode(password):
    decoded = ''
    for char in password:
        temp = int(char) - 3
        if temp < 0:
            temp += 10
        decoded += str(temp)
    return decoded


if __name__ == "__main__":
    while True:
        print('Menu')
        print('---------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')

        user_input = int(input('Please enter an option:'))

        if user_input == 1:
            password = input('Please enter your password to encode:')
            encoded = encode(password)
            print(encoded)
            print('Your password has been encoded and stored!')
        if user_input == 2:
            decoded = decode(encoded)
            print(f'The encoded passowrd {encoded}, and the original password is {decoded}.')
        if user_input == 3:
            exit()




