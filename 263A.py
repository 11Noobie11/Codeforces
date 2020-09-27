#263A

l1_string=input()
l2_string=input()
l3_string=input()
l4_string=input()
l5_string=input()
moves=0
l1=l1_string.split()
l2=l2_string.split()
l3=l3_string.split()
l4=l4_string.split()
l5=l5_string.split()
for i in range(5):
    if l1[i]=="1":
        moves=abs(i-2)+2
    elif l2[i]=="1":
        moves=abs(i-2)+1
    elif l3[i]=="1":
        moves=abs(i-2)
    elif l4[i]=="1":
        moves=abs(i-2)+1
    elif l5[i]=="1":
        moves=abs(i-2)+2
    else:
        continue
print(moves)
