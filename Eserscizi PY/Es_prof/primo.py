
from operator import truediv


n=int(input(f"inserire numero: "))
"""
t=0
for i in range(1,n+1):
    if (n%i==int(0)):
        t=t+1
    else:
        pass

if t<=2:
    print(f"è un numero primo")
else:
    print(f"non è un numero primo")

"""
def isprimo(n):
    for i in range (2, int(n**0.5)+1):
        if n%i==0:
            return False
        return True

if(isprimo(n)==True):
    print("primo")
else:
    print("non primo")