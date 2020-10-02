#1A

p=input()
l=p.split()
n=int(l[0])
m=int(l[1])
a=int(l[2])
if m%a==0: 
    x=m//a 
else: 
    x=m//a+1 
 
if n%a==0: 
    y=n//a 
else: 
    y=n//a+1 
print(x*y)
