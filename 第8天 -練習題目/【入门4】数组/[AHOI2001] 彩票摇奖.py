n = int(input())
lotto = list(map(int,input().split()))
arr = []
fin =[0]*7
for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(n):
    hit = 0
    for k in range(7):
        if arr[i][k] in lotto:
            hit+=1
    if hit!=0:
        fin[(7-hit)]+=1

print(' '.join(map(str,fin)))

#if arr[i][k] in lotto 檢查陣列裡面是否有該值            
            

# for i in range(n):
#     hit = 0
#     for k in range(7):
#         for j in range(i+1,n):
#             if arr[i][k]==lotto[j]:
#                 hit+=1
#     fin[(6-hit)]+=1