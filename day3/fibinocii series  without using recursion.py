#fibinocii number without recursion
n=int(input("enter a number:"))
n1=0
n2=1
if(n<0):
    print("no series is possible")
else:
    for i in range(0,n-1):
        n3=n1+n2
        n1=n2
        n2=n3
    print(n3)
    
