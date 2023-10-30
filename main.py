# Authors: Alexander Wang + Lucas Gavrielides

# Importing the different function/methods from separate files!
import decode
import encode


# menu/user prompting
while True:
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit\n')

    option = int(input('Please enter an option: '))
    # User picked options are parsed by the if statements!
    if option == 1:
        original_password = input('Please enter your password to encode: ')
        if len(original_password) == 8 and original_password.isnumeric():
            encoded_password = encode(original_password)
            print('Your password has been encoded and stored!\n')
            continue
        else:
            print('Invalid Input! Password contains more than 8 digits or contains a letter! \n ')

    if option == 2:
        # decode is called here and it responds with both your encoded password and your decoded one
        print(f'The encoded password is {encoded_password}, and the original password is {decode.decode(encoded_password)}.\n')
    if option == 3:
        # ends the code
        break



