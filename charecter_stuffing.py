n=input().split()
n1=" "
l=len(n)
f1='DLESTX'
F2='DLEETX'
for i in range(l):
    if(n[i]=='DLE'):
        n[i]+=" "+n[i]
    elif(n[i]=='STX'):
        n[i]+=" "+n[i]
    elif(n[i]=='DLESTX'):
        n[i]+=" "+n[i]
    elif(n[i]=='DLEETX'):
        n[i]+=" "+n[i]
    elif(n[i]=='ETX'):
        n[i]+=" "+n[i]
for i in range(l-1):
    n[i]+=" "+'DLE'
for i in range(l):
    if(i==0):
        n1+=n[i]
    else:
        n1+=" "+n[i]
print(n1)
