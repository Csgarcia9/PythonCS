import random

chars = "abcdefghijklmnopqrstuv123456789"

password = ""

for i in range(10):
    password += random.choice(chars)

print(f"La clave generada es: {password}")