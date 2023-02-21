"""
Scrivi un programma in Python che chieda un numero all’utente e gli comunichi se questo numero è divisibileper 3 oppure no. 
Per verificare la divisibilità può essertiutile l’operatore resto %. L’espressione a%b calcola il re- sto della divisione tra a e b.
"""

n=int(input("inserire numero: "))

if n%3==0:
    print(f"è divisibile per 3")
else:
    print(f"non è divisibe per 3")

