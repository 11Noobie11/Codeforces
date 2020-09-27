#1095A
#Repeating Cipher
length=int(input())
cipher=input()
text=""
n=0
for i in range(0,length//3+1):
    n+=i
    if n>=length:
        break
    text+=cipher[n]
print(text)
