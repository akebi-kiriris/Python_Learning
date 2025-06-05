n=int(input())

for i in range(n):
    for k in range(n):
        print(chr(65+(i+k)%26),end="")
    print()

