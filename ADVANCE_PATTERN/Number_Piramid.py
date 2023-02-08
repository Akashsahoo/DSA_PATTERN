n = 5
for row in range(1,n+1):
    for space in range(1,n-row+1):
        print(" ",end="")
    for number in range(1,row+1):
        print(str(row)+" ",end ="")
    print()