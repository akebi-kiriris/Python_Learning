n = int(input())
president = []

for i in range(n):
    president.append((i+1,int(input())))
president.sort(key=lambda x: (x[1]))

print(president[-1][0])
print(president[-1][1])
#或是
# winner = max(president, key=lambda x: x[1])
# print(winner[0])
# print(winner[1])

