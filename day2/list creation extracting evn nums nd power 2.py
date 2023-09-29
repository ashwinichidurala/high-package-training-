
#create an 1-d array ,it should contain number between 10 to 30,extract an print even numbers and
#2 power values
li=[]
li1=[]
li2=[]
l=list(map(int,input().split(",")))
s=int(input("enter array size:"))
for i in range(s):
    n=int(input(":"))
    if n>=l[0] and n<=l[1]:
        li.append(n)
    else:
        print(n,"is out of range")
for i in li:
    if i%2==0:
        print(i,end=" ")
for i in range(l[1]):
    li1.append(2**i)
print()
for i in li:
    if i in li1:
        print(i,end=" ")
