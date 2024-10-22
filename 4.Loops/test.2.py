fruits = ['banana','grapes','apple','orange']

print("-------------")  

# Printing till orange
for x in fruits :
    print(x)
    if x=='apple':
        break

print("-------------")    

# Printing till apple    
for x in fruits :
    if x=="apple" :
        break
    print(x)
    
print("-------------")    
    
# Continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print("-------------")   

# Range   
for x in range(2,11,2):
    print(x)  

print("-------------")  
