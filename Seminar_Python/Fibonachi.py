"""Задача No31. Решение в группах
Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
Input: 7 Output: 21"""
#n = 7
"""def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fib(n-1) + fib(n-2)
print(fib(7))"""
index = 7

def fibonacci(index):
    if index <= 1:
        return 1
    return fibonacci(index-1) + fibonacci(index-2)
print(fibonacci(7))