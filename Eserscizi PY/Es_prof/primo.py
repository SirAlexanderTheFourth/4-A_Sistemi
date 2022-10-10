n=int(input(f"inserire numero: "))
t=0
i=1
for i in range(n-i):
    if (n%i==int(0)):
        t=t+1
    else:
        pass

if t==2:
    print(f"è un numero primo")
else:
    print(f"non è un numero primo")


