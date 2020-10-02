#1031A

n=input()
l=n.split()
w=int(l[0])
h=int(l[1])
k=int(l[2])
s=(w*h)-(w-2)*(h-2)
a=0
b=0
c=0
for i in range(2,k+1):
    a=w-(4*(i-1))
    b=h-(4*(i-1))
    c=(a*b)-(a-2)*(b-2)
    s+=c
print(s)
