import socket 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s2=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
my_adress=("0.0.0.0", 8000)
next_adress=("192.168.1.133",8000)
s.bind(my_adress)

while True:
    text_recived, adress=s.recvfrom(4096)
    print(f"ricevuto messaggio: {text_recived.decode()} da {adress}")
    input("")
    s2.sendto(text_recived, next_adress)
