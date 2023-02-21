#Scrivi programma in python in cui inizializzi la lista
#X=[0,1,2,3,5,6,7,8] e poi che:
#crei due nuove liste contenenti ciascuna una delle due metà deda lista
#aggiungi il valore S alla Ista contenente la prima metà
x=[1,2,3,5,6,7,8]
l=len(x)
x1=x[0 : (l//2)]
x2=x[(l//2)::]
print(x1)
print(x2)