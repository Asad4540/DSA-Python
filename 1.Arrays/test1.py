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