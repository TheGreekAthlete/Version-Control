
def encode(password):
    return ''.join([str((int(item) + 3) % 10) for item in password])

# logic to decode the encoded string once provided
def decode(password):
    return ''.join([str((int(item) - 3) % 10) for item in password])

# menu/user prompting

while True:
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit\n')

    option = int(input('Please enter an option: '))

    if option == 1:
        original_password = input('Please enter your password to encode: ')
        if len(original_password) == 8 and original_password.isnumeric():
            encoded_password = encode(original_password)
            print('Your password has been encoded and stored!\n')
            continue
        else:
            print('Invalid Input! Password contains more than 8 digits or contains a letter! \n ')

    if option == 2:
        print(f'The encoded password is {encoded_password}, and the original password is {original_password}.\n')
    if option == 3:
        # ends the code
        break



