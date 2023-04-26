import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_adress=("127.0.0.1", 5001)

while True:
    text=input("Scrivi un messaggio: ")
    if text=="exit":
        break
    text_b=text.encode()
    s.sendto(text_b, server_adress)
    text_recived, adress=s.recvfrom(4096)
    print(f"ricevuto messaggio: {text_recived.decode()} da {adress}")

s.close()