
lista1=["a","b","c","d"]
lista2=[1,2,3,4]
#for su lista1 C-style
for k in range(0,len(lista1)):
    print(k, lista1[k])
print("\n")

#for su lista1 Pytonic
for element in lista1:
    print(element)
print("\n")

#for su lista1 con enumerate
for item in enumerate(lista1):
    print(item)

print("\n")

#for su lista1 e lista2 Pytonic (zip())
for i,n in zip(lista1, lista2):
    print(i, n)
print("\n")
"""
#for su lista1 e lista2 C-style (range)
for i in range():
    
print("\n")
"""
diz={ 1:"ciao", 2:"non", 3:"so", 4:"cosa", 5:"scrivere"}

#for su diz usando items()
for k, v in diz.items():
    print(k, v)
print("\n")

#for su diz semza items()
for k in diz:   
    print(diz[k])
