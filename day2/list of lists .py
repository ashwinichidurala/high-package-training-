#polynomial complexity :O(n 2)
def genarate_lists_of_lists(n):
    table_list=[]
    for num in range(n):
        row=[]
        for i in range(n):
            row.append(i)
        table_list.append(row)
    return table_list
print(genarate_lists_of_lists(10))
