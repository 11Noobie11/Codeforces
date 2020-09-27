#705A

n=int(input())
a="I hate"
b="I love"
result=[]
for i in range(n):
    if i%2==0:
        result.append(a)
        if i==n-1:
            result.append(" it")
        else:
            result.append(" that ")
    else:
        result.append(b)
        if i==n-1:
            result.append(" it")
        else:
            result.append(" that ")
for i in result:
    print(i,end="")
