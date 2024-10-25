# The provided code stub reads and integer,n , from STDIN. For all non-negative integers i<n, print i square.

n = int(input("enter a no : "))

for i in range(n):
    print(f"{i * i}")