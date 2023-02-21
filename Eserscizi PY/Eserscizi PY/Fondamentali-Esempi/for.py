lista=[110,12,45,66]

#modo preferito (pytinico)
for elemento in lista:
    print(elemento, end="-")

print("\n")

#modo C-style
for i in range(0,len(lista)):
    print(lista[i], end="-")
