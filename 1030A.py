#In Search of an Easy Problem
#1030A

n=int(input())
a=input()
op=a.split()
x=0
for i in op:
    if i=="1":
        x=-1
        break
if x==-1:
    print("HARD")
else:
    print("EASY")
    
