import random
import string

def password_generator():
    length = int(input("enter the password length you need:"))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    print("passwoed is:", password)
password_generator()