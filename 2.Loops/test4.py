# Write a Python program to find the smallest & Greatest of three numbers. Prompt the user to enter the three numbers and print the smallest of the three.

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))

if num1 > num2 and num1 > num3 :
    print(num1,"or num1 is greatest of all")
elif num2> num1 and num2 > num3 :
    print(num2,"or num2 is greatest of all")
elif num3> num1 and num3 > num2 :
    print(num3,"or num3 is greatest of all")
else :
    print("All numbers are equal")
    
    
if num1 < num2 and num1 < num3 :
    print(num1,"or num1 is smallest of all")
elif num2 < num1 and num2 < num3 :
    print(num2,"or num2 is smallest of all")
elif num3 < num1 and num3 < num2 :
    print(num3,"or num3 is smallest of all")
else :
    print("All numbers are equal")
    