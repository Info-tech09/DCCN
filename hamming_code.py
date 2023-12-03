def hammingcode(l,i,r):
    no_of_ones=0
    for j in range(2**r):
        if(j>len(l)):
            break
        check=str(bin(j))
        check=check[2:]
        if(len(check)<r):
            check="0"*(r-len(check))+check
        if(check[len(check)-i]=="1"):
            if(l[len(l)-j]=="1"):
                no_of_ones+=1
    if(no_of_ones%2==0):
        l[-(2**(i-1))]="0"
    else:
        l[-(2**(i-1))]="1"
string=input("enter the string:")
m=len(string)
r=1
while True:
    if(2**r>=(m+r+1)):
        break
    r+=1
l=[0 for i in range(m+r)]
for i in range(r):
    l[2**i-1]="p"
l=l[::-1]
for i in range(len(l)):
    if(l[i]==0):
        l[i]=string[0]
        string=string[1:]
for i in range(1,r+1):
    hammingcode(l,i,r)
s=""
for i in l:
    s+=i
print(s)
