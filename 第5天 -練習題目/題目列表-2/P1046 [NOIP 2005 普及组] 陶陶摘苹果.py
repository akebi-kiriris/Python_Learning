arr = list(map(int,input().split()))
h = int(input())+30
check = 0
for i in range(10):
    if h>=arr[i]:
        check+=1

print(check)