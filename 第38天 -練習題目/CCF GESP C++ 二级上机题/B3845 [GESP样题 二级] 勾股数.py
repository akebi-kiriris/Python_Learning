n = int(input())

check = 0

for a in range(1,n+1):
    for b in range(a,n+1):
        cp=a**2+b**2
        c=int(cp**0.5)   
        if c>n:
            break
        if c * c == cp:
            check+=1

print(check)