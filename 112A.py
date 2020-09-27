#112A

string1=input()
string2=input()
lower1=string1.lower()
lower2=string2.lower()
x=0
for i in range(len(lower1)):
    if ord(lower1[i])>ord(lower2[i]):
        x=1
        break
    elif ord(lower1[i])<ord(lower2[i]):
        x=-1
        break
    else:
        continue
print(x)
