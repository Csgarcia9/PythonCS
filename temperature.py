def fahrenheit_to_celsius(Fahrenheit):
    celsius = (Fahrenheit - 32) * (5/9)
    print("Los grados de Fahrenheit a Celsius es: " , " > " ,  round(celsius,2),"°")
    

def celsius_to_fahrenheit(celsius):   
    fahrenheit = (celsius * (9/5)) + 32
    print("Los grados de Celsius a Fahrenheit es: " , " > " ,  round(fahrenheit, 2),"°")
     

Fahrenheit = float(input("Digite los grados en fahrenheit: "))     
Celsius = float(input("Digite los grados en celsius: "))

fahrenheit_to_celsius(Fahrenheit)
celsius_to_fahrenheit(Celsius)
