arr = list(input().split())
time=list(map(int,arr[:3]))

print(sum(time[x]*60**(2-x) for x in range(3))+(43200 if arr[3]=="P" else 0))
