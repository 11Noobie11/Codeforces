#1208A

def XORinacci(a,b,n): 
    if n==0:  
        return(a)  
    if n==1:  
        return(b) 
    if n==2:  
        return(a^b)  
    return XORinacci(a,b,n%3)
x=[]
p=int(input())
for i in range(p):
    y=input()
    l=y.split()
    a=int(l[0])
    b=int(l[1])
    n=int(l[2])
    x.append(XORinacci(a,b,n))
for i in x:
    print(i)
