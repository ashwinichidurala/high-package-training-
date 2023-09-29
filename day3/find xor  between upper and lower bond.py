#calculate xor  from lower bound to upper bound
ar=int(input())
lb=int(input())
x=0
for i in range(ar,lb+1):
    x=x^i
print(x)
