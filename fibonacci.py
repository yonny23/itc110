#8.1 p 279 Fibonacci Series

def fibonacci(n):
    a = 0
    b = 1
    for i in range (0, n):
        fib = a
        a = b
        b = fib + b
    return a

for c in range(0, 15):
    print(fibonacci(c))
