from random import randint


def cifrado_cesar(palabra, desplazamiento):
    resultado = ''
    for letra in palabra:
        if letra.isalpha():
            ascii_inicial = ord('a') if letra.islower() else ord('A')
            nueva_letra = chr((ord(letra) - ascii_inicial +
                              desplazamiento) % 26 + ascii_inicial)
            resultado += nueva_letra
        elif letra.isdigit():

            nuevo_digito = str((int(letra) + desplazamiento) % 10)
            resultado += nuevo_digito
        else:
            resultado += letra
    return resultado


# Palabra a encriptar
palabra_original = input("Digite la palabra a encriptar: ")

# Desplazamiento para el cifrado
desplazamiento = randint(1, 10)
print(f"El desplazamiento fue de {desplazamiento}")
# Encriptar la palabra
palabra_encriptada = cifrado_cesar(palabra_original, desplazamiento)
print("Palabra encriptada:", palabra_encriptada)


def descifrado_cesar(palabra_encriptada, desplazamiento):
    resultado = ''
    for letra in palabra_encriptada:
        if letra.isalpha():
            ascii_inicial = ord('a') if letra.islower() else ord('A')
            nueva_letra = chr((ord(letra) - ascii_inicial -
                              desplazamiento) % 26 + ascii_inicial)
            resultado += nueva_letra
        elif letra.isdigit():

            nuevo_digito = str((int(letra) - desplazamiento) % 10)
            resultado += nuevo_digito
        else:
            resultado += letra
    return resultado

# Palabra a encriptar

# Desplazamiento para el cifrado


# Encriptar la palabra
palabra_desencriptada = descifrado_cesar(palabra_encriptada, desplazamiento)
print("Palabra desencriptada:", palabra_desencriptada)
