arr = list(map(int,input().split()))

cock_price = arr[0]
hen_price = arr[1]
chick_price = arr[2]
money = arr[3]
max_num = arr[4]
total = 0
#deepseek改進
#cock_price, hen_price, chick_price, money, num = map(int, input().split())
#cock_price, hen_price, chick_price, money, max_num = arr

for cock in range(max_num+1):
    for hen in range(max_num-cock+1):
        chick=(max_num-cock-hen)
        if chick >= 0 and chick%chick_price==0 and cock*cock_price + hen*hen_price + chick//chick_price == money:
            total+=1

print(total)
            