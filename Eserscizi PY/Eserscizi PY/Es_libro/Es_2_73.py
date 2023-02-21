"""
Scrivi un programma in Python che chieda un numero all’utente e gli comunichi se questo numero è divisibile per 2, o per 3, o per 5, o per nessuno di essi. 
Per verificare la divisibilità può esserti utile l’operatore resto %. L’espressione a%b calcola il resto della divisione tra a e b.
"""
n=int(input("inserire numero: "))
if n%2==0:
    print(f"è divisibile per 2")
elif n%3==0:
    print(f"è divisibile per 3")
elif n%5==0:
    print(f"è divisibile per 5")
else:
    print(f"non è divisibile")