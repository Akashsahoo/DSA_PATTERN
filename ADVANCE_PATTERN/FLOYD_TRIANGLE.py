n = 5
number_value = 1
for row in range(n):
    for number in range(row+1):
        print(number_value,end=" ")
        number_value +=1
    # for space in range(n-row-1):
    #     print("",end="")
    print()
    
    

