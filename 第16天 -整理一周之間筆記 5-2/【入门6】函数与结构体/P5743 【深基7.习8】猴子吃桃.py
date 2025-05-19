def cal(num):
    return (num+1)*2


n = int(input())
num=1
for i in range(n-1):
    num=cal(num)
print(num)
