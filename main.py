# lab 6 by Hannah

def looping_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")
    print("Please enter an option:", end=' ')
    option = int(input())
    return option


def encode(password):
    encoded_password = ""
    for letter in password:
        if letter.isdigit():
            letter = int(letter)
            letter += 3
            if letter >= 10:
                letter -= 10
            letter = str(letter)
            encoded_password += letter
    print('Your password has been encoded and stored!')
    return encoded_password

def decode(encoded_password):
    pass

if __name__ == '__main__':
    option = looping_menu()
    while option != 3:
        if option == 1:
            print('Please enter your password to encode:', end = ' ')
            password = input()
            encoded_password = encode(password)
        if option == 2:
            pass
        option = looping_menu()