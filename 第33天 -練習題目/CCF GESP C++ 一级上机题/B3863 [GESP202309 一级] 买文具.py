n = [int(input()) for i in range(4)]
summ=n[0]*2+n[1]*5+n[2]*3
diff = n[3]-summ
if diff>=0:
    print("Yes")
    print(diff)
else:
    print("No")
    print(abs(diff))