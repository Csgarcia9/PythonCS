# Definir una función para encontrar la verdad en un mensaje secreto.
# Cambia las letras de una palabra en una cantidad específica para descubrir la palabra oculta
def lasso_letter( letter, shift_amount ):
    letter_code = ord(letter.lower())
    a_ascii = ord('a')
    alphabet_size = 26
    true_letter_code = a_ascii + (((letter_code - a_ascii) + shift_amount) % alphabet_size)
    decoded_letter = chr(true_letter_code)
    return decoded_letter




def lasso_word(word, shift_amount):
    decoded_word = ""
# Este bucle for itera cada letra en el parámetro palabra
    for letter in word:
        # La función lasso_letter() se invoca con cada letra y la cantidad de turno
# El resultado (la letra decodificada) se almacena en una variable llamada letra_decodificada
        decoded_letter = lasso_letter(letter, shift_amount)
        # El valor decodificado_letra se agrega al final del valor decodificado_palabra
        decoded_word = decoded_word + decoded_letter

    return decoded_word
    

# Try to decode the word "terra"
print( "Shifting Ncevy by 13 gives: \n" + lasso_word( "Ncevy", 13 ) )
print( "Shifting gpvsui by 25 gives: \n" + lasso_word( "gpvsui", 25 ) )
print( "Shifting ugflgkg by -18 gives: \n" + lasso_word( "ugflgkg", -18 ) )
print( "Shifting wjmmf by -1 gives: \n" + lasso_word( "wjmmf", -1 ) )










