# нахождение факториала
def fact(x):
    if x == 1:
        return 1
    return fact(x - 1) * x


print(fact(4))
print(fact(7))

# числа Фибоначчи
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(5))
print(fib(6))
print(fib(7))