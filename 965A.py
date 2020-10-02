#965A

from math import *
a=input()
l=a.split()
k=int(l[0])
n=int(l[1])
s=int(l[2])
p=int(l[3])
result=ceil((ceil(n/s)*k)/p)
print(result)
