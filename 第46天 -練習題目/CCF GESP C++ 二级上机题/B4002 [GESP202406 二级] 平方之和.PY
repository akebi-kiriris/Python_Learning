n = int(input())

for i in range(n):
    temp = int(input())
    check=0
    for x in range(1,int(temp**0.5)+1):
        y = temp-x*x
        if int(y**0.5)==y**0.5 and y>0:
            check=1
            break
    if check==1:
        print("Yes")
    else:
        print("No")