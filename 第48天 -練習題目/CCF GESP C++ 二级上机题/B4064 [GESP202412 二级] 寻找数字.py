n = int(input())

for i in range(n):
    temp = int(input())
    check = temp**0.25
    if int(temp**0.25)==temp**0.25:
        print(int(temp**0.25))
    else:
        print(-1)