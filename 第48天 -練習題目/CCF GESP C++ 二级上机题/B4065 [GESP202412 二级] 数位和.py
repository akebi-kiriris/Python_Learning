n = int(input())
temp = 0

for i in range(n):
    num = sum(int(x) for x in input())
    if num>temp:
        temp = num
    
print(temp)