#82A

names=['Sheldon','Leonard','Penny','Rajesh','Howard']
n=int(input())
x=1
while n>=x*5:
    n-=x*5
    x*=2
n=n-1
n=n//x
print(names[n])
