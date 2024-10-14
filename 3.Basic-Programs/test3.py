#Program to print multiplication table by taking a input from user

def multiply_table (num) :
    print(f"Multiplication Table for {num} : ")
    
    for i in range(1,11) :
        print(f"{num} * {i} = {num * i }")
        
#Input from user

number = int(input("Enter a number : "))
multiply_table(number)

