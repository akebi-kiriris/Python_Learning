def rec(n):
    if n!=1:
        return n*rec(n-1)
    return n

n = int(input())

print(rec(n))