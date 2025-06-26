l = int(input())
arr = []
    
for i in range(2,l):
    check = 1
    for k in range(2,i):
        if i%2==0:
            check = 0
            break
        if i%k==0:
            check = 0
            break
    if check==1:
        arr.append(i)
    if sum(arr)>l:
        arr.pop()
        break

if l!=1:
    print('\n'.join(map(str,arr)))
print(len(arr))


