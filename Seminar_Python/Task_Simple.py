

"""определить с помощью рекурсии, число Х является простым
def is_simple_num(x):
    if x <= 1:
        return False
    
    for i in range(2, x):
        if x % i == 0:
            return False
    
    return True

print(is_simple_num(6))"""

i = 2
count = 0
def prosto(n, i=2):
    if n ==2 or i *i>n:
        return True
    if n%i ==0:
        return False
    return prosto(n, i+1)
    
print(prosto(10))