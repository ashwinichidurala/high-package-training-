#check given number is even or odd using xor
n=int(input("enter a number:"))
if(n&1==0):
    print("even")
else:
    print("odd")
