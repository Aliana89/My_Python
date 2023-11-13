"""Напишите функцию, которая принимаетодно число и проверяет , является ли оно простым"""


def is_simple(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

print(is_simple(6))
