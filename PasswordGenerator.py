import random
#import time

class Error(Exception):
    pass
class InputError(Error):
    pass
class Passwords:
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+='."
    population = alphabet_upper + alphabet_upper + numbers + symbols

    @classmethod
    def generate(cls,i):
        return "".join(random.sample(list(cls.population), i))

    @classmethod
    def max_password_len(cls):
        return len(cls.population)

print(f"Please enter the length of passwords (maximum length of passwords is {Passwords.max_password_len()}): ")
while True:
        num = int(input())
        if (num > Passwords.max_password_len()):
            print("Length of passwords too long. Maximum length of passwords is {Passwords.max_password_len()}. Please Retry.")
        else:
            print(Passwords.generate(num), '\n')
            break
while True:
    try:
        response = input("Do you want to generate another password? Y/N \n").capitalize()
        if (response == "Y"):
            print(Passwords.generate(num), '\n')
            continue
        elif (response == "N"):
            print('Program terminated.')
            break
        else:
            raise InputError
    except InputError:
        print("Please enter the correct input. Y/N")
        continue

        #time.sleep(2)    # Pause 2 seconds
