import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
letters_choice = int(input("How many letters would you like in your password?\n"))
password = ""
for number in range(letters_choice + 1):
    password += random.choice(letters)
# print(alphabets)
symbols_choice = int(input("How many symbols would you like?\n"))
# char = ""
for number in range(symbols_choice + 1):
    password += random.choice(symbols)
# print(char)
numbers_choice = int(input("How many numbers would you like?\n"))
# num = ""
for number in range(numbers_choice + 1):
    password += str(random.choice(numbers))
password_list = list(password)
print(password_list)
random.shuffle(password_list)
print(password_list)
print("Your password is:", ''.join(password_list))

