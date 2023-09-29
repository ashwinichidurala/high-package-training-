#individual digits sum
num=int(input())

s=0
while(num>0):
    rem=num%10
    s+=rem
    num=num//10
print(s)

n=int(input())
s=0
temp=n
for i in range(1,n,n//10):
    rem=s+int(temp%10)
    temp=temp//10
    
print(s)
    

