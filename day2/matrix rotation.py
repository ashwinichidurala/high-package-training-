#program to rotate a matrix 90 degrees
"""mt=[[1,2],[3,4]]
print(mt)
res=[[0,0],[0,0]]
for i in range(len(mt)):
    for j in range(len(mt[0])):
       res[j][i]=mt[i][j]

print(mt)"""
"""for i in range(5-1,-1,-1):
    print(i)"""
n=int(input("enter number of rows:"))
m=int(input("enter number of columns:"))
matrix=[]
matrix1=[]
for i in range(n):
    a=[]
    for i in range(m):
        x=int(input("enter value:"))
        a.append(x)
    matrix.append(a)
for i in range(n):
    for j in range(m-1,-1,-1):
        print(matrix[j][i],end=" ")
    print()





