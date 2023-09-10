def factura_luz(consumo):
    
    if consumo <= 200:
        factura = (consumo * 6.17) + 127.83
        return round(factura,2) 
    elif consumo <= 300:
        factura = ((consumo - 300)* 8.71) + (200 * 6.17) + 127.83
        return round(factura,2) 
    elif consumo > 300:
        restante1 = 100 * 8.71
        restante2 = (consumo - 300) * 13.04
        factura = restante1 + restante2 + (200 * 8.71) + 127.83
        return round(factura,2) 
        
consumo = float(input("Digite el consumo electrico: "))  
if consumo < 1:
    print("No posee consumo electrico")
else:    
    print("Su factura es de: ",factura_luz(consumo), "Pesos")
