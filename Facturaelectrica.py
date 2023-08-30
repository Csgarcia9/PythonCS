def factura_luz(consumo):
    
    if consumo <= 200:
        factura = (consumo * 8.62) + 128.96
        return round(factura,2) 
    elif consumo <= 300:
        factura = ((consumo - 300)* 10.93) + (200 * 8.62) + 128.96
        return round(factura,2) 
    elif consumo > 300:
        restante1 = 100 * 10.93
        restante2 = (consumo - 300) * 13.26
        factura = restante1 + restante2 + (200 * 8.62) + 128.96
        return round(factura,2) 
        
consumo = float(input("Digite el consumo electrico: "))  
if consumo < 1:
    print("No posee consumo electrico")
else:    
    print("Su factura es de: ",factura_luz(consumo), "Pesos")
