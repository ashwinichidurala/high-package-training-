
def add(data):
    count=0
    for i in arr:
        count=count+i
    return count 

arr=list(map(int,input().split(" ")))
print(add(arr))
        
