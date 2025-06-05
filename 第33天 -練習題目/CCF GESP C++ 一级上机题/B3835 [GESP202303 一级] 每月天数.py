n,m = map(int,input().split())
check = 0

month = (31,28,31,30,31,30,31,31,30,31,30,31)

if n%4==0 and n%100!=0:
    check=1
elif n%100==0 and n%400==0:
    check=1

print(month[m-1]+(1 if m==2 and check==1 else 0))
