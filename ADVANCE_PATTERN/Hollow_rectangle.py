n = 4
for row in range(1,n+1):
    for col in range(n+1):
        if row == 1 or row == n or col == 0 or col == n:
            print("*",end='')
        else:
            print(" ",end="")
    print('')
