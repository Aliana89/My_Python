def f(x):
    return x
print(f(5))

f1 = lambda x:x 
print(f1(5))
print((lambda x:x) (5))
number = "1 2 3 4 5"
n1 = number.split()
print(n1)
n2 = list(map(int, n1))
print (n2)
n3 = list(map(lambda x:x*3, n2))
print (n3)
n4  = list(filter(lambda x:x %2 == 0,n3))
print (n4)
n4  = list(filter(lambda x:2 ,n3))
print (n4)