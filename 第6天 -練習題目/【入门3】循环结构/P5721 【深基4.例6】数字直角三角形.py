n = int(input())
start = 1
fin = n
h = 1
while h<=n:
    for i in range(start,fin+1):
        print(f"{i:02d}",end='')
    start = fin+1
    fin+=(n-h)
    h+=1
    print('')
#12345
#start=5+1=6
#fin=9
#h=2
#6789
#start=10
#fin=12