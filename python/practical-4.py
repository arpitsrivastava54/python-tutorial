number = int(input("enter whole number : "))

if(number == 1 or number == 0):
    print("not a prime number")
else:
    flag = False
    for x in range(2,(number//2)+1):
        if(number%x == 0):
            print("Not a prime number")
            flag = True
    if(flag == False):
        print("prime Number")
            
            
        

