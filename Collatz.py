c0 = int(input("Digite un numero natural: "))
# Se valida que sea mayor que 0 para inicial
if c0 <= 0:
    print("El numero tiene que ser mayor que cero")
else:
# este else empiza a contar cuantos pasos se dan
    paso = 0
    while c0 != 1:       # Este while se asegura que mientras sea diferente de 1 siga
        if c0 % 2 == 0:  # Evalua el restante para hacer el primer calculo
            c0 = c0 // 2 
        else: # Este else hace el calculo para llegar a 1 
            c0= 3 * c0 + 1
        paso += 1   
        print (c0)
    print (f"\nSe alcanzó 1 en {paso} pasos.")               

