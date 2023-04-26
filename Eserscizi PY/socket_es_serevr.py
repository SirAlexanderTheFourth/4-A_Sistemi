import socket 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
my_adress=("0.0.0.0", 5001)
s.bind(my_adress)

while True:
    text_recived, adress=s.recvfrom(4096)
    print(f"ricevuto messaggio: {text_recived.decode()} da {adress}")
    s.sendto(b"OK", adress)


s.close()