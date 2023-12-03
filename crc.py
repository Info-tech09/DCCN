s=input("enter divisor")
sL=len(s)
z="0"
w="0"
for i in range(sL-1):
    w=w+"0"
for i in range(sL-2):
    z=z+"0"
s1=input("enter data")
s2=s1+z
def exor(a,b):
    n=len(a)
    c=""
    for i in range(n):
        if a[i]==b[i]:
            c=c+"0"
        else:
            c=c+"1"
    return c
l=len(s1)
def crc(l,s2,s,sL,w):
    for i in range(l):
        if s2[0]=="1":
            e=exor(s,s2[0:sL])
        else:
            e=exor(s2[0:sL],w)
        s2=e[1:]+s2[sL:]    
    return e
f=crc(l,s2,s,sL,w)
print("sender data")
print(f)
sf=str(f)
rs=s1+sf[1:]
f=crc(l,rs,s,sL,w)
print("reciver data")
print(f)
fa=str(f)
if "1" in fa:
    print("error")
else:
    print("no error")
