# Import ASCII font art library
from pyfiglet import figlet_format

figlet = figlet_format
# text = input("Enter your text: ")
# print(figlet(text, font='standard'))

with open('categories.txt', 'r') as file:
    categories = file.read().splitlines()
    print(categories)