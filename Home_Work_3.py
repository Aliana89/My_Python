n = 385916
S =(n//1000)
suml= int(S/100)+int(S%100/10)+int(S%10)
R =(n%1000)
sumr = int(R/100)+int(R%100/10)+int(R%10)
if (suml == sumr):
    print('yes')
else:
    print('no')    