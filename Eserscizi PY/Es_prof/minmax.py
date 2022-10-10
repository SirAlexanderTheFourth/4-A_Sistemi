from ast import literal_eval


lista=[110,12,45,23,66]
max=lista[0]
min=lista[0]
for elemento in lista[1:]:
    if(elemento<min):
        min=elemento
    else:
        pass
    if(elemento>max):
        max=elemento
    else:
        pass

print(f"minimo: {min}, massimo: {max}")