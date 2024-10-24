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
    digit = 0
    new_password = ''
    for i in range(len(encoded_password)):
        digit = int(encoded_password[i]) - 3
        if digit < 0:
            digit = int(encoded_password[i]) + 10 - 3
            new_password += str(digit)
        else:
            new_password += str(digit)
    return new_password

if __name__ == '__main__':
    option = looping_menu()
    while option != 3:
        if option == 1:
            print('Please enter your password to encode:', end = ' ')
            password = input()
            encoded_password = encode(password)
            print(encoded_password)
        elif option == 2:
            password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {password}")
        option = looping_menu()