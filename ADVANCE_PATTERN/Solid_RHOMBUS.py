n = 5
for row in range(1,n+1):
    for space in range(1,n-row+1):
        print(" ",end="")
    for star in range(n):
        print('*',end="")
    print()