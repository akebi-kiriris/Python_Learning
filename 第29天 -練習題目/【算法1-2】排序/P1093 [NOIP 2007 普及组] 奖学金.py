n = int(input())
students = []
for i in range(1, n+1):
    c, m, e = map(int, input().split())
    total = c + m + e
    students.append((i, total, c))

#按照總分、語文、學號排，如果總分同則用語文，語文同則用學號。
students.sort(key=lambda x: (-x[1], -x[2], x[0]))

for id, total, _ in students[:5]:
    print(id, total)
