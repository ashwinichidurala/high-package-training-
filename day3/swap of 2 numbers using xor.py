#swap of 2 numbers using xor
a=100
b=200
print("a:",a,"b:",b)
a=a^b
b=a^b
a=a^b
print("a:",a,"b:",b)
