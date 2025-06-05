#有一題不知為何wa。但分數100
from math import gcd
a,b,c = map(int,input().split())

oriset = {1,2,3,4,5,6,7,8,9}
arr=[]

m = gcd(gcd(a, b), c)
a = int(a/m)
b = int(b/m)
c = int(c/m)


start = max(100 // a + (1 if 100 % a else 0), 1) 
end = min(999 // a, 999 // b, 999 // c) 
for i in range(123,988):
    A = a*i
    B = b*i
    C = c*i

    if not (100 <= A <= 999 and 100 <= B <= 999 and 100 <= C <= 999):
        continue
    
    digits = str(A) + str(B) + str(C)
    if '0' in digits: 
        continue
    
    tempset = set(int(d) for d in digits)
    if tempset==oriset:
        arr.append((A,B,C))
    
if arr:
    for i in sorted(arr): 
        print(*i)
else:
    print("No!!!")
    