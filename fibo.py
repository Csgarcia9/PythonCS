def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        a = 1
        b = 1
        for i in range(3, n + 1):
            temp = a + b 
            a = b 
            b = temp 
            print(i , b, sep=" >> ")

n = 10
resultado = fibo(n)     

print(f"El resultado de la serie es: {resultado}")


"""def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):
    print(n, "->", fib(n))"""