k = int(input())
sum = 0   #金幣總和
check = 1 #每級天數
coin = 1  #每級金幣
day = 1   #日期總和
temp = 0  #當前級數已過天數




while day<=k:
    if temp<check:
        sum +=coin
        temp+=1
    else:
        coin+=1
        sum+=coin
        temp=1
        check+=1
    day+=1

print(sum)


#deepseek解
# k = int(input())
# sum = 0
# day = 0
# coin = 1  # 當前級數

# while day < k:
#     for _ in range(coin):  # 每級發放 coin 天
#         if day == k:
#             break
#         sum += coin
#         day += 1
#     coin += 1

# print(sum)
#6天
#1天 sum=1 temp=1 check=1 coin=1 day=2 
#2天 sum=3 temp=1 check=2 coin=2 day=3
#3天 sum=5 temp=2 check=2 coin=2 day=4
#4天 sum=