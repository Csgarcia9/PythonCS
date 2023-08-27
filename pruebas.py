bloques_totales = int(input("Ingrese la cantidad de bloques disponibles:"))

# Inicialización de la variable para que incrementen luego
altura = 0
bloques_utilizados = 0

# While que hace que mientras haya bloques totales el bucle se repita
while bloques_utilizados + altura + 1 <= bloques_totales:
    altura += 1 # aqui se sube uno a la altura y guarda el tamaño de la pila de bloques
    bloques_utilizados += altura # aqui se sube un bloque mas que a la altura para simular que incrementa la linea anterior 

print("La altura de la pirámide que se puede construir es: ", altura)

