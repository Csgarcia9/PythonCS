# Se crea para asignar las palabras sin vocales
word_without_vowels = ""

user_word = input("Ingresa una palabra: ")
user_word = user_word.upper()


for letter in user_word:
    if letter in 'AEIOU':
        continue
    word_without_vowels += letter
    

print("Palabra sin vocales ",word_without_vowels)

