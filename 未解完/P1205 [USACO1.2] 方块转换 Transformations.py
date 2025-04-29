#gpt 優雅寫法
# n = int(input())
# arr = [list(map(str, input().split())) for _ in range(n)]

n = int(input())
arr = []*n*2


for i in range(n*2):
    arr.append(list(map(str,input().split())))


while True:
    break


print(''.join(map(str,arr)))