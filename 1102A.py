#1102A

n=int(input())
a=[]
if n%2==0:
    a=[n-1,n]
    if n>2:
        if a[1]%4==0:
            print(0)
        else:
            print(1)
    else:
        print(1)
else:
    a=[n,n+1]
    if a[1]%4==0:
        print(0)
    else:
        print(1)
    
    
