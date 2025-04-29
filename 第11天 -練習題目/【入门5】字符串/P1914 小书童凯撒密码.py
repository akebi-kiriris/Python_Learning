n = int(input())
s = input()
arr = []*n


for i in s:
    if ord(i)+n<=ord("z"):
        arr.append(chr(ord(i)+n))
        continue
    arr.append(chr(ord(i)+n-26))

print(''.join(map(str,arr)))