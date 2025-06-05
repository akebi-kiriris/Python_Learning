sh = int(input())
sm = int(input())
ss = int(input())
ts = int(input())

eh = (sh*3600+sm*60+ss+ts)//3600
em = ((sh-eh)*3600+sm*60+ss+ts)//60
es = ((sh-eh)*3600+(sm-em)*60+ss+ts)

print(eh,em,es)