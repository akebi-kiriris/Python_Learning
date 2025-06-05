n,m = map(int,input().split())
total= 0

for i in range(n+1,m):
    if i%4==0 and i%100!=0:
        total+=i
    elif i%100==0 and i%400==0:
        total+=i

print(total)