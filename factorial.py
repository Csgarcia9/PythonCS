def factorial_funcion(n):
    if n < 0:
        return None
    if n < 2:
        return 1    
    producto = 1
    for i in range(2, n + 1):
        producto*= i
    return producto


for n in range(1, 6):
    print(n , factorial_funcion(n))



"""def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)

for n in range(1, 6):
    print(n, factorial_function(n))"""