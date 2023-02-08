n = 5
for row in range(n):
    for number in range(1,n-row+1):
        print(number,end="")
    # for space in range(row+1):
    #     print(" ",end="")
    print()