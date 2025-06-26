n = int(input())

for i in range(n):
    snum = input()
    num = int(snum)
    t = 0
    for i in snum:
        t+=int(i)**len(snum)
    if num==t:
        print("T")
    else:
        print("F")