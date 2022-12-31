# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# get the number of times you want to get the letters
# get the number of times you want to get the symbols and numbers
letter = ""
number = ""
symbol = ""
final_password = ""
for count in range(0, nr_letters + 1):
    # count_rand = random.randint(0, nr_letters)
    letter += random.choice(letters)
print(letter)

for count in range(0, nr_symbols + 1):
    # count_rand = random.randint(0, nr_letters)
    number += random.choice(numbers)
print(number)

for count in range(0, nr_numbers + 1):
    # count_rand = random.randint(0, nr_letters)
    symbol += random.choice(symbols)
print(symbol)

password = letter + number + symbol
passwords = []
for instances in password:
    passwords.append(instances)

random.shuffle(passwords)
for instance in passwords:
    final_password += instance

print(final_password)