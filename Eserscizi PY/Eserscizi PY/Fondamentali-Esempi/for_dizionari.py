dizionario={"w":"avanti", "a":"sinistra", "s":"dietro", "d":"destra"}
for k,v in dizionario.items(): #ciclo per chiave e valore
    print(k, v)

for k in dizionario: #ciclo per chiave
    print(k)

for k in dizionario: #ciclo per chiave ma uso valore
    print(dizionario[k])

lista=[]
comando = "avanti"

for k,v in dizionario.items():
    if v == comando:
        lista.append(k)
    else:
        pass

print(lista)