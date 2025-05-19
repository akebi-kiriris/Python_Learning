n = int(input())
arr = []
distance = 0
for i in range(n):
    x,y,z = map(int,input().split())
    arr.append((x,y,z))

arr.sort(key=lambda x:(x[2]))
for i in range(n - 1):
    x1, y1, z1 = arr[i]
    x2, y2, z2 = arr[i + 1]
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    distance += (dx ** 2 + dy ** 2 + dz ** 2) ** 0.5
print(f"{distance:.3f}")