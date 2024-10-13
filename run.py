# Import ASCII font art library
from pyfiglet import figlet_format

figlet = figlet_format
# text = input("Enter your text: ")
# print(figlet(text, font='standard'))


def main():

    with open('categories.txt', 'r') as file:
        categories = file.read().splitlines()
    with open('fonts-first', 'r') as file:
        fonts = file.read().splitlines()

    print("Welcome to text art generator!")
    print("You can use it to add style to footer of your emails or as banners in forums")
    print()
    print("Choose the category of font:\n", categories)

    while input() != "first":
        print('Please choose one of the listed categories: ', categories)
    else:
        print("Choose desired font:\n", fonts)
        while input() != "font1":
            print("Please choose one of the listed fonts: ", fonts)
        else:
            text = input("Enter your text: ")
            print("Loading amazing art...")
            print(figlet(text, font='standard'))

            while True:
                input("Another try? Enter key: Y / N\n")
                if input() == "Y":
                    main()
                elif input() == "N":
                    break
                else:
                    print("wrong input")
main()