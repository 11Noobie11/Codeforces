#71A

n=int(input())
l=[]
for i in range(n):
    string=input()
    l.append(string)
for i in range(n):
    n=l[i]
    text=""
    if len(n)>10:
        text+=n[0]+str(len(n)-2)+n[len(n)-1]
    else:
        print(n,end="")
    print(text)
