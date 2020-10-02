#1096A

n=int(input())
t=[]
for i in range(n):
    s=input()
    a=s.split()
    l=int(a[0])
    r=int(a[1])
    t.append([l,l*2])
for j in range(n):
    print(t[j][0],t[j][1])
