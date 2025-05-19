def is_prime(num):
    if num==2:
        return 1
    if num % 2 == 0:
        return 0
    for i in range(3,int(num**0.5)+1):
        if num%i==0:
            return 0
    return 1




def cal (num):
    for i in range(2,num//2):
        if is_prime(i) and is_prime(num-i):
            print(f"{num}={i}+{num-i}")
            return 0
    print(f"{num}={int(num//2)}+{int(num//2)}")

n = int(input())

for i in range(4,n+1,2):
    cal(i)