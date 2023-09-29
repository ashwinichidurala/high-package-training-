#once occurance of a number

def findsingle(ar,n):
    res=ar[0]
    for i in range(1,n):
        res=res^ar[i]
    return res
ar=list(map(int,input().split(" ")))
print(findsingle(ar,len(ar)))
