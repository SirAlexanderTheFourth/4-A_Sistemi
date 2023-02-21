n1=input(f"inserisci un numero: ")
n2=input(f"inserisci un secondo numero: ")
l=[0,0,0,0]
l[0]=((n1**2)+(n2**2))
l[1]=(n1+n2)**2
l[2]=(n1**2)-(n2**2)
l[3]=(n1-n2)**2
print(l[0::])