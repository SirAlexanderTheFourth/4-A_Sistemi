#es 1
s="chikakok"
print(s[::2])

#es 2
n=int(input("numero: "))
lista=[1]*n
lista[0],lista[-1]=0,0
print(lista)

#es 3
n=int(input("numero: "))
l=[]
for i in range(1,n+1):
    l.append(i)
print(l)

#alternativa es 3
l1=[]
l1=[i for i in range(1,n+1)]
print (l1)