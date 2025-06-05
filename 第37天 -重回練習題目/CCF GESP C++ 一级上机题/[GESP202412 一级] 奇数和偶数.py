n = int(input())
odd=0
even=0

for i in range(n):
    check = int(input())
    if check%2==0:
        even+=1
    else:
        odd+=1

print(odd,even,sep=" ")