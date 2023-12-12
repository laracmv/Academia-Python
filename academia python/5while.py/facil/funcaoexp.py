def calcula_euler(x,n):
    euler = 1
    fat = 1
    i = 2
    while i <= (n+1):
        fat = fat * i
        euler += x**(n-1)/fat
        i+=1
    return euler

print(calcula_euler(2,2))


































