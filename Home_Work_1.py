n = int(123)
n1 = int(n/100)
n2 = int(n%100/10)
n3 = int(n%10)
res = (n1+n2+n3)
print(f"{res} ({n1} + {n2} + {n3})")

# res= (n//100 + n//10%10 + n%10)