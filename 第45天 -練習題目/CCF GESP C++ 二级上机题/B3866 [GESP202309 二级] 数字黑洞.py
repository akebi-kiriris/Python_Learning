n = int(input())
check = 0

while n!=495:
    arr = []
    arr.append(n//100)
    arr.append(n//10%10)
    arr.append(n%10)
    arr= sorted(arr)
    sma = arr[0]*100+arr[1]*10+arr[2]
    lar = arr[2]*100+arr[1]*10+arr[0]
    n = lar-sma
    check+=1

print(check)

