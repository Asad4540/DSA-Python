# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

heros = ['spiderman','thor','hulk','ironman','captain america']

#Length of the list
length = len(heros)
print(length)

# Ans2 adding black panther at the end of the list
heros.append('black panther')
print(heros)

#Ans 3 remove black panther from the list first 
heros.remove('black panther')
print(heros)

#and then add it after 'hulk'
heros.insert(heros.index('hulk') + 1, 'black panther')
print(heros)

del heros[1:3]
heros.insert(heros.index('spiderman')+1,'doctor strange')
print(heros)

#sort the heros list in alphabetical order 
heros.sort()
print(heros)