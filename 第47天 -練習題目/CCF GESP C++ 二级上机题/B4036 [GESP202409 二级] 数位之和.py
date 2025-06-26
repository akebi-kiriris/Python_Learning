n = int(input())

for i in range(n):
    temp = input()
    summ = sum(int(x) for x in temp)
    if summ%7==0:
        print("Yes")
    else:
        print("No")