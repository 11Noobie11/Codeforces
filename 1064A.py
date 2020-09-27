#1064A

s=input()
l=s.split()
a=int(l[0])
b=int(l[1])
c=int(l[2])
def side_of_triangle(a1,b1,c1):
    while a1+b1<=c1:
        if a1<b1:
            a1+=1
        else:
            b1+=1
    while b1+c1<=a1:
        if b1<c1:
            b1+=1
        else:
            c1+=1
    while a1+c1<=b1:
        if a1<c1:
            a1+=1
        else:
            c1+=1
    return(a1,b1,c1)
a1,b1,c1=side_of_triangle(a,b,c)
print(abs(a-a1)+abs(b-b1)+abs(c-c1))
