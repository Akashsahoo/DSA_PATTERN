n = 5
for row in range(1,n+1):
    for space in range(1,n-row+1):
        print(" ",end="")
    for number in range(row,0,-1):
        print(number,end="")
        
    for number in range(2,row+1):
        print(number,end="")
    print()
