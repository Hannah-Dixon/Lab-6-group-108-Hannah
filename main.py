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


if __name__ == '__main__':
    option = looping_menu()
    while option != 3:
        if option == 1:
            pass
        if option == 2:
            pass
        option = looping_menu()