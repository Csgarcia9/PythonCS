def factura_luz(consumo):
    
    if consumo <= 200:
        factura = consumo * 5
        return factura 
    elif consumo <= 290:
        factura = ((consumo - 200)* 8) + (200 * 5)
        return factura 
    elif consumo > 290:
        restante1 = 90 * 8
        restante2 = (consumo - 290) * 11
        factura = restante1 + restante2 + (200 * 5)
        return factura 
        
consumo = float(input("Digite el consumo electrico: "))  
if consumo < 1:
    print("No posee consumo electrico")
else:    
    print("Su factura es de: ",factura_luz(consumo), "Pesos")
