n = [int(input()) for i in range(4)]

start = n[0] * 60 + n[1]
end = n[2] * 60 + n[3]
print(end-start)