def triangularnumber(Number):
    sum = 0
    flag = 1
    for i in range(Number):
        sum = sum + i 
        if(sum == Number):
            flag = 0
            print(f"The {Number} is a Triangular Number")
    if(flag == 1):
        print(f"The {Number} is a not Triangular Number")

Number = int(input("Enter the Number: "))
triangularnumber(Number)