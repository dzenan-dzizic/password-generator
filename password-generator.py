import string
import secrets
import datetime
import time
import os


def generate_rn():

    choice = secrets.choice(range(1, 5))

    if choice == 1:
        random_number_uc = secrets.choice(range(0, 26))#upercase letters
        variable = upper_letters[random_number_uc]
        return str(variable)
    
    elif choice == 2:
        random_number_lc = secrets.choice(range(0, 26))#lowercase letters
        variable = lower_letters[random_number_lc]
        return str(variable)
    
    elif choice == 3:
        random_number_num = secrets.choice(range(0, 10))#numbers
        variable = numbers[random_number_num]
        return str(variable)
    
    elif choice == 4:
        random_number_sym = secrets.choice(range(0, 30))#symbols
        variable = special_symbols[random_number_sym]
        return str(variable)
 
    
#uppercase letters of the english alphabet
upper_letters = list(string.ascii_uppercase)


#lowercase letters of the english alphabet
lower_letters = list(string.ascii_lowercase)


numbers = [0,1,2,3,4,5,6,7,8,9]

special_symbols = list("!@#$%^&*()_+-={}[]|:;\"'<>,.?/~`")


os.system('cls' if os.name == 'nt' else 'clear')
print("Password generator")
print("Security levels: Basic (1), Secure (2), Ultra Secure (3).")
user_input = int(input("Choose a security level for password. Enter a number (1-3): "))

if user_input == 1:
    rm = secrets.choice(range(12,17))

elif user_input == 2:
    rm = secrets.choice(range(16,25))

elif user_input == 3:
    rm = secrets.choice(range(25,32))



password = [None] * rm

for i in range(rm):
     
    password[i] = generate_rn()


os.system('cls' if os.name == 'nt' else 'clear')
current_time = datetime.datetime.now()
print(f"Starting password generator at", str(current_time)[:-7])
print("")
time.sleep(3)

s = ''

for c in password:
    s += c

print("Password generated: ", s)
print("")
print("\n" * 4)#for creating some empty space

