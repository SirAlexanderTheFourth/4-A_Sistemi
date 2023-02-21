import random

l_Ali=[random.randint(1,6) for _ in range(10)]
l_Bob=[random.randint(1,6) for _ in range(10)]

f=open(".\Es_libro\casuali.txt", "w")

for i, k in zip(l_Ali, l_Bob):
    f.write(f"{i}, {k}\n")

f.close()

#tabella di pitagora
def make_tabella_pitagorica():
    return[[numero * indice for numero in range(1,11)]for indice in range(1,11)]

def write_file(bomeFile, tabella_pitagorica):
    file = open(".\Es_libro\pitagorica.txt", "w")
    for riga in tabella_pitagorica:
        file.write(f'{')