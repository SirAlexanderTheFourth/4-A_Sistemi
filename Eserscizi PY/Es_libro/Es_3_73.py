"""
Scrivi un programma che permetta all’utente di effettuare le quattro operazioni aritmetiche. 
Per prima cosa chiede all’utente quale operazione desidera eseguire (0: somma, 1: sottrazione, 2: moltiplicazione: 3 divisione), 
poi chiede all’utente due numeri e stampa il risultato dell’operazione.
"""
def somma(n1,n2):
    return (n1+n2)

def sottrazione(n1,n2):
    return (n1-n2)

def moltiplicazione(n1,n2):
    return (n1*n2)

def divisione(n1,n2):
    return (n1/n2)

opzioni={0:somma, 1:sottrazione, 2:moltiplicazione, 3:divisione}

op=int(input("scegliere azione:\n0-somma\n1-sottrazione\n2-moltiplicazione\n3-divisione\n"))
n1,n2=int(input("inserire numero: ")), int(input("inserire numero: "))
r=opzioni[op](n1,n2)
print(r)
