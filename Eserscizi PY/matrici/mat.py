
file = open("mat.csv", "r")
lista_righe = file.readlines()
file.close()
lista = []
n = 0
map_num = []

for riga in lista_righe[0:]:
    # linea senza \n
    riga_senza_n = riga[:-1]
    lista_rig = riga_senza_n.split(",")
    lista.append(lista_rig)


for lista_n in lista:
    lista_l = []
    for element in lista_n:
        if element == '0':
            lista_l.append(n)
            n += 1
        else:
            lista_l.append(-1)
    print(lista_l)
    map_num.append(lista_l)
print(map_num)
