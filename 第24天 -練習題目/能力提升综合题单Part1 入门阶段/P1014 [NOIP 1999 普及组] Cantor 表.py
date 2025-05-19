n= int(input())
sum = 0
check = 0
pos = 0
de = 0 #分母
nu = 0 #分子
if n ==1:
    sum = 1
    check = 1


for i in range(1,n+1):
    sum+=i
    if sum>=n:
        #算出在第幾層
        check= i
        #算出在該層的第幾個
        pos = n-(i-1)*i//2
        break
if check%2==1:
    nu = check-pos+1
    de = pos
else:
    nu = pos
    de = check+1-pos
print(f"{nu}/{de}")

#n=6
#sum=1+2+3=6 check=3 pos=3
#n=5
#sum=1+2+3=6 check=3 pos=2
#n=7
#sum=1+2+3+4=10 check=4 pos=1
#在該層前有i*(i-1)/2個，n-該層前=剩多少個也就是第幾個


    