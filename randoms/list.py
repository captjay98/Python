a = [7,2,5,1,3,1,5,2,
    5,8,1,5,7,2,7,4,1,
    5,3,7,5,8,1,7]
b = [7,1,5,2, 8]

for x in b:
    while x in a:
        j = a.index(x)
        a.pop(j)
        
print(a)

s