Number = int(input("Enter the Number: "))
Sum = 0
flag = 1
for i in range(Number):
    Sum = Sum + i
    if(Sum == Number):
        flag = 0;
        print(f"The {Number} is Triangular Number")

if(flag == 1):
    print(f"The {Number} is not Triangular Number")