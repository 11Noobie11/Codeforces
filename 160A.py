#160A

n=int(input())
string=input()
l=string.split()
x=0
for i in range(n):
    l[i]=int(l[i])
l.sort(reverse=True)
if n==1:
    coins=1
else:
    for i in range(n):
        x+=l[i]
        y=0
        coins=0
        coins=i+1
        for j in range(i+1,n):
            y+=l[j]
        if x>y:
            break

print(coins)
