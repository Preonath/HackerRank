s=map(int,input().split())
n=map(int,input().split())
sl=list(s)
nl=list(n)
sm=0
sn=0
for i ,j in zip(sl,nl):
    if(i>j):
        sm+=1
    elif(j>i):
        sn += 1
    else:
        sn+=0
        sm+=0
print(sm,sn)