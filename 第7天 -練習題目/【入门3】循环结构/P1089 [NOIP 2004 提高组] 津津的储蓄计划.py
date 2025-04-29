#2025/4/23 7.46-8.29
arr = []
for _ in range(12):
    arr.append(int(input()))

money = 0
save = 0
month = 1
mom = 0
for i in arr:
    money+=300
    #先判斷破產了沒
    if money<i:
        break
    #判斷能不能存，存多少
    while money-i>=100 :
        money-=100
        save +=1
    money -=i
    mom +=save*100
    month +=1
    save = 0

if month==13:
    print(int(mom*1.2)+money)
else:
    print("-",month,sep='')