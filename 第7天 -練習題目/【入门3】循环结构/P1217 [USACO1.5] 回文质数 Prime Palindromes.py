# #012345 6
# def even_check(num):
#     lent = len(num)
#     pos = 0
#     while pos<lent//2:
#         if num[pos] != num[lent-1-pos]:
#             return 0
#         pos+=1
#     return 1

# #01234 5
# def odd_check(num):
#     lent = len(num)
#     pos = 0
#     while pos<lent//2:
#         if num[pos] != num[lent-1-pos]:
#             return 0
#         pos+=1
#     return 1


# a,b = map(int,input().split())

# al = len(str(a))
# bl = len(str(b))
# arr=[]
# check = 0
# if al == 1:  
#     ast = 1
# else:
#     ast = 10**(al-1)

# #產生數字，判斷是否為回文，下限為10**(al-1)，上限為10**(bl)-1
# for i in range(ast,10**(bl),2):
#     if len(str(i))%2==0:
#         if even_check(str(i))!=0:
#             arr.append(i)
#     else: 
#         if odd_check(str(i))!=0:
#             arr.append(i)

# #檢查是否為質數
# primes = []
# for i in arr:
#     is_prime = True
#     for k in range(2, int(i**0.5) + 1):
#         if i % k == 0:
#             is_prime = False
#             break
#     if is_prime:
#         primes.append(i)
# arr = primes

# #檢查是否在範圍內
# while len(arr)!=0 and arr[0] < a:
#     del arr[0]
# while len(arr)!=0 and arr[-1] > b:
#     del arr[-1]


# print('\n'.join(map(str, arr)))
    
    
#參考deepseek產生回文，未抄
def rever(a,b):
    rev = []
    #奇
    for i in range(1,100000):
        s = str(i)
        temp = int(s + s[-2::-1]) 
        if temp<a:
            continue
        if temp>b:
            break
        rev.append(temp)
    #偶    
    for i in range(1,100000):
        s = str(i)
        temp = int(s + s[::-1]) 
        if temp<a:
            continue
        if temp>b:
            break
        rev.append(temp)
        
    return rev    



a,b = map(int,input().split())

arr = rever(a,b)
    
#檢查是否為質數
primes = []
for i in arr:
    is_prime = True
    if i != 2 and i % 2 == 0:
        continue
    for k in range(2, int(i**0.5) + 1):
        if i % k == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
arr = primes
arr = sorted(arr)



print('\n'.join(map(str, arr)))


#deepseek產生回文解
# def rever(a, b):
#     rev = []
#     for i in range(1, 100000):
#         s = str(i)
#         pal_odd = int(s + s[-2::-1])
#         pal_even = int(s + s[::-1])
#         for temp in (pal_odd, pal_even):
#             if temp < a:
#                 continue
#             if temp > b:
#                 continue
#             rev.append(temp)
#     return rev  



