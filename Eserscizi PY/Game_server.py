import socket 
import random
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
my_adress=("0.0.0.0", 5001)
s.bind(my_adress)

file=open("parole.txt","r")
righe=file.readlines()
file.close()
parola=righe[random.randint(0,1175)]

while True:
    text_recived, adress=s.recvfrom(4096)
    text=text_recived.decode()
    print(text)
    correction=""
    k=0
    if text == parola:
        s.sendto(f"La parola '{parola}' è stata indovinata da {adress}", "255.255.255.0")
    for l in text :
        if l== parola[k]:
            correction=correction + l
        else:
            correction=correction + "_"
        
        if k==len(text)-1:
            n=len(parola)-len(text)
            for n in range(1, n):
                correction=correction + "_"
            break
        else:
            pass

        if k>len(text):
            break
        else:
            k=k+1
        

    s.sendto(correction.encode(), adress)

