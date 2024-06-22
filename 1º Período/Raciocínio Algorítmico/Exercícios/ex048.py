# Implemente uma função recursiva capaz de retornar o n-ésimo
# elemento da série de Fibonacci.
#   • Fibonacci = 1, 1, 2, 3, 5, 8, 13, 21, ...

def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n - 2) + fibo(n - 1)
    
num = int(input("Digite um número: "))
nesimo = fibo(num)
print(nesimo)