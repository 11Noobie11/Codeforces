#282A

n=int(input())
X=0
for i in range(n):
    statement=input()
    statement_list=statement.split("X")
    for i in statement_list:
        if i=="++":
            X+=1
        elif i=="--":
            X-=1
        else:
            continue
print(X)
