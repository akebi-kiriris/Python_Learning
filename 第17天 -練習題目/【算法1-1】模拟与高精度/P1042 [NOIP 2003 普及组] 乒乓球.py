arr = []
while True:
    line = input().strip()
    if "E" in line:  
        arr.extend(line[:line.index('E')])
        break
    arr.extend(line) 

arr = [c for c in arr if c in ('W', 'L')]

score = [0] * 2
score_21 = [0] * 2
#從頭開始讀，若分數到了11分就印出一次分數，並且重製分數重新計分。
for i in arr:
    if i=="W":
        score[0]+=1
    else:
        score[1]+=1
    if max(score) >= 11 and abs(score[0]-score[1])>=2:
        print(f"{score[0]}:{score[1]}")
        score = [0] * 2
print(f"{score[0]}:{score[1]}")
print()
        
for i in arr:
    if i=="W":
        score_21[0]+=1
    else:
        score_21[1]+=1
    if max(score_21) >= 21 and abs(score_21[0]-score_21[1])>=2:
        print(f"{score_21[0]}:{score_21[1]}")
        score_21 = [0] * 2
print(f"{score_21[0]}:{score_21[1]}")
    


        