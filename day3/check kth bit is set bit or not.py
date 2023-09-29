n=int(input("enter a number:"))
pos=int(input("enter bit pos:"))
if n&(1<<n-1)==1:
    print("yes set bit")
else:
    print("not a set bit")
    

