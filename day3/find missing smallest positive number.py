#without using sorting function
#after creating an array find out the smallest missing positive integer
li=list(map(int,input().split(" ")))
temp=0
sl=[]
sl.sort
"""for i in sl:
    if i>temp:
        temp=si[i]
        si[i]=si[i+1]
        si[i+i]=temp"""
    
for i in range(len(li)):
    if i not in li:
        sl.append(i)
        
print(sl[0])


        
        
