s,v = map(int,input().split(' '))
c_time = s/v

#計算所需時間
if c_time/int(c_time)!=1:
    c_time = int(c_time)+1
    
a_time = 60*24
hour = (a_time-c_time -10)//60
minute = (a_time-c_time -10)-60*hour


f_hour = int(8+hour)
f_minute = int(minute)
if(f_hour>=24):
    f_hour-=24

print(f"{f_hour:02}"+":",end='')
print(f"{f_minute:02}")
#print(f"{f_hour:02}:{f_minute:02}")即可


  