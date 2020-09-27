#1061A

string=input()
l=string.split()
n=int(l[0])
S=int(l[1])
count=S//n
x=count*n
if x<S:
    x+=n
    count+=1
print(count)
