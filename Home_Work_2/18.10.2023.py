s = 12
p = 27
x = 1
y = s-x
p = x * y
s = x + y


for x in range(0, s//2+1):
    if x*y == p: 
        print(x,y)                
    y = s-x
    print(x,y) 
    x += 1       
         
    
   

