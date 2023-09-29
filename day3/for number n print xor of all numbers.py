"""#given n number print xor of all numbers
#time complexity O(n)
n=int(input("enter a number :"))
xor=0
for i in range(1,n+1):
    xor=xor^i
print(xor)"""


#reducing time complexity to O(1)
n=int(input("enter a number :"))
xor=0
if n%4==0:
    print(n)
elif n%4==1:
    print(1)
elif n%4==2:
    print(n+1)
elif n%4==3:
    print(0)
    



