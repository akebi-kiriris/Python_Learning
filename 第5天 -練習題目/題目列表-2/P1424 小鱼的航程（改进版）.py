x,n = map(int,input().split())
check = 1 #經過天數
week = {0,1,2,3,4,5,6} #一周
sum = 0 #距離

#先把第一周不完全的算完

#若是6或7則加到下周一
if x ==6 :
    check+=2
elif x ==7:
    check+=1
elif n<=5:
    sum+=250*n
    check= check+n
else:
    sum+=250*(6-x)
    check =check+(6-x)+2

#算接下來的
while check<=n:
    for i in week:
        if i!=5 and i!=6:
            sum+=250
        if check==n:
            check+=1 #要加1
            break
        check+=1

print(sum)
    

#3 10
#sum=750 check=6
#0 sum=1000 check=7
#1 sum=1250 check=8
#2 sum=1500 check=9
#3 sum=1750 check=10
#4 sum=2000 check=11 脫離










# for i in range(n):
#     if day==6:
#         day+=1
#         break
#     if day==7:
#         day+=1
#         break
    