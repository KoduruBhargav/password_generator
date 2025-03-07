import random
# store data
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#enter input
name = input("Enter your name: ")
print(f"Hi {name}, Welcome to the Password Generator!")
number_of_letters = int(input("How many letters would you like in your password?\n"))
number_of_symbols = int(input(f"How many symbols would you like?\n"))
number_of_numbers = int(input(f"How many numbers would you like?\n"))

#edge cases - not empty
entry = True
if number_of_letters <= 0:
    print("Letters should not be empty.")
    entry = False
if number_of_symbols <= 0:
    print("Symbols should not be empty.")
    entry = False
if number_of_numbers <= 0:
    print("Numbers should not be empty.")
    entry = False

# check to continue or stop execution based on bool(entry variable)
if not entry:
    exit()

#create empty list to store
password = []

# Here, k: The number of random elements you want to choose.
password += random.choices(letters, k= number_of_letters)
password += random.choices(symbols, k= number_of_symbols)
password += random.choices(numbers, k= number_of_numbers)

#shuffel the password
random.shuffle(password)

#print password
print(f"{''.join(password)}")