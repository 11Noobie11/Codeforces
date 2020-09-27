#339A

string=input()
l=string.split("+")
l.sort()
result=""
for i in range(len(l)):
    result+=l[i]
    if i!=len(l)-1:
        result+="+"
print(result)
