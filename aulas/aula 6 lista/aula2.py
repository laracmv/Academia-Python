a = [
    [1,2,3], 
    [4,5,6]
]

b = [
    [-4,6,2],
    [2,3,0]
]

c = [
    [0,0,0], [0,0,0]
]

lin = 0
while lin < len(a): 
    col = 0
    while col < len(a[lin]):
        c[lin][col] = a[lin][col] + b[lin][col]
        col += 1
    lin +=1
print(c)

