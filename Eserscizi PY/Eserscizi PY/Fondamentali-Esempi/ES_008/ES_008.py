parola = input("inserire parola: ")
#parola[3]='?'
parola=parola[:2]+'?'+parola[3:]
#le stringhe sono immutabili, non si possono modificare, solo rassegnare
print(parola)