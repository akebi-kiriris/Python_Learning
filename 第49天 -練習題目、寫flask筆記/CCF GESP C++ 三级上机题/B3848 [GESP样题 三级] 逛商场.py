n = int(input())
arr = list(map(int, input().split()))
x = int(input())

count = 0

for price in arr:
    if x >= price:
        x -= price
        count += 1

print(count)
