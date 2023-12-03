data=input("enter binary message in the format of 2^")
l=len(data)//2
p1=data[:l]
p2=data[l:]
def find_bin_val(a,b):
    sum = bin(int(a, 2) + int(b, 2))
    p=str(sum[2:])
    if len(p)>len(a):
      sum=bin(int(p,2)+1)
    return str((sum[2:]))
def once_com(d):
    j=""
    for i in d:
        if i=="1":
            j=j+"0"
        else:
            j=j+"1"
    return j
def exor(a,b):
    n=len(a)
    c=""
    for i in range(n):
        if a[i]==b[i]:
            c=c+"0"
        else:
            c=c+"1"
    return c
d=find_bin_val(p1,p2)
d2=once_com(d)
lis=[p1,p2,d2]
print("sender")
for i in lis:
    print(i)
d3=once_com(d2)
d4=exor(d2,d3)
d5=once_com(d4)
print("after checking at reciver side")
if "1" in d5:
    print ("error message")
else:
    print("error free")
