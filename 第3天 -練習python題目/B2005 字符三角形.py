block = input()
space = 2
q = 1

for i in range(3):
    print(' '*space,end='')
    print(block*q)
    q+=2
    space-=1