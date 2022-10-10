#Scrivi un programma in Python che permetta all’utente di inserire due numeri qualsiasi. Crea un dizionario in cui salvi la media aritmetica e la media geometrica dei due numeri. Stampa il dizionario.
from math import sqrt

n1=int(input(f"inserire numero: "))
n2=int(input(f"inserire secondo numero: "))
sol={"aritmetica":(n1*n2)/2, "geometrica":sqrt(n1*n2)}
print(sol["aritmetica"])
print(sol["geometrica"])
print(sol)
