#96A

players=input()
n=0
for i in range(len(players)):
    try:
        if players[i]=="0" and players[i+1]=="0" and players[i+2]=="0" and players[i+3]=="0" and players[i+4]=="0" and players[i+5]=="0" and players[i+6]=="0":
            n=1
        if players[i]=="1" and players[i+1]=="1" and players[i+2]=="1" and players[i+3]=="1" and players[i+4]=="1" and players[i+5]=="1" and players[i+6]=="1":
            n=1
    except:
        break
if n==1:
    print("YES")
else:
    print("NO")
