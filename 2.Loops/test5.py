# Ask user to enter a Age and check if the user is eligible to vote

age = int(input("Enter your age : "))

if age > 18 : 
    print("you are eligible to vote")
elif age == 18 :
    print("you are just completed 18")
else :
    print("you are not eligible to vote")
