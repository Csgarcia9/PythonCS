def fahrenheit_to_celsius(Fahrenheit):
    celsius = (Fahrenheit - 32) * (5/9)
    print(f"Los grados de Fahrenheit a Celsius es:  > {round(celsius,2)}°C")
    

def celsius_to_fahrenheit(celsius):   
    fahrenheit = (celsius * (9/5)) + 32
    print(f"Los grados de Celsius a Fahrenheit es > {round(fahrenheit,2)}°F")
     

Fahrenheit = float(input("Digite los grados en fahrenheit: "))     
Celsius = float(input("Digite los grados en celsius: "))

fahrenheit_to_celsius(Fahrenheit)
celsius_to_fahrenheit(Celsius)
