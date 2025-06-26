space = 2
diamond = 1
check = 0

for i in range(5):
    print(" "*space,end='')
    print("*"*diamond)
    if space == 0:
        check=1
    if check ==0:
        space-=1
        diamond+=2
    if check ==1:
        space+=1
        diamond-=2
        
#ai給的改良
# for i in range(5):
#     spaces = abs(2 - i)
#     stars = 5 - 2 * abs(i - 2)
#     print(' ' * spaces + '*' * stars)
