p = int(input("Enter your principle amount : "))
r = int(input("Enter your rate of interest : "))
t = int(input("Enter your tenure/years : "))

simpleInterest = p*r*t/100

print(f"Your simple intertest for {t} years is : Rs {simpleInterest} with {r}% of interest rate")
