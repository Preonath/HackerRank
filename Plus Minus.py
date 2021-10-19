n= int(input())
s=map(int,input().split())
sl=list(s)
p=0
nn=0
o=0
l=len(sl)
for i in sl:
    if(i>0):
        p+=1
    elif(i<0):
        nn+=1
    else:
        o+=1
print(p/l)
print(nn/l)
print(o/l)
