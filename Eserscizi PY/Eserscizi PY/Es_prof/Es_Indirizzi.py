class IPadress():
    def __init__(self,ip_stringa):
        self.ip_dec = ip_stringa
        self.ip_bin = None
        self.ip_Broadcast = None
        self.ip_Rete = None
    
    def dec2bin(self):
        lista_bin=self.ip_dec.split(".")
        lista_grupp = [int(Bin)for Bin in lista_bin]
        s = ""
        self.ip_bin = ""
        for gruppo in lista_grupp:
            temp= bin(gruppo)[2:]
            temp = "0"*(8-len(temp))+temp
            self.ip_bin = self.ip_bin+temp
            s = s +temp + "."
        return s[:-1]

    def ip_broadcast(self,subnet_mask = "/22"):
        num = int(subnet_mask[1:])
        sub_bin = ""
        sub_bin = "0"*num + "1"*(32-num)
        """
        for w in range(0,32):
            if(w < num):
                sub_bin = sub_bin+"0"
            else:
                sub_bin = sub_bin+"1"
        """
        temp = ""
        for a in range(0,32):
            if(a % 8 == 0):
                temp =temp + "."
            else:
                pass
            if(self.ip_bin[a] == "0" and sub_bin[a] == "0"):
                temp = temp + '0'
            else:
                temp = temp + '1'

        self.ip_Broadcast=temp[1:]    
        return self.ip_Broadcast

    def sub_conv(self, subnet_mask):
        if(subnet_mask[0]=='/'):
            pass
        else:
            self.dec2bin()
        

    

    def ip_rete(self,subnet_mask = "/22"):
        num = int(subnet_mask[1:])
        sub_bin = ""
        sub_bin = "1"*num + "0"*(32-num)
        temp = ""
        for a in range(0,32):
            if(a % 8 == 0):
                temp =temp + "."
            else:
                pass
            if(self.ip_bin[a] == "1" and sub_bin[a] == "1"):
                temp = temp + '1'
            else:
                temp = temp + '0'

        self.ip_Rete=temp[1:]
            
        return self.ip_Rete
"""
    def sottorete(self, n_sub, subnet_mask):
        n_IP=2**(32 - int(subnet_mask[1:]))
        n_sottoreti=0
        if(n_IP%n_sub!=0):
         for i in range(2, n_IP):
              if(n_IP%i==0 && i>n_sub):
                   n_sottoreti=i
                  break
        else:
            n_sottoreti=n_sub

        n_ip_sub=n_IP/n_sottoreti
        for i in range(0,n_sub-1):
            for j int range(0, n_ip_sub):
           """     
 

  

    
def bin2dec(Ip):
    lista_bin_Rete=Ip.split(".")
    d = ""
    for num in lista_bin_Rete:
        temp = int(num,2)
        d = d + str(temp) +"."
    return d[:-1]
            
    #def toList(self):
    #    lista_stringhe = self.ip_dec.split(".")
    #    return[int(gruppo)for gruppo in lista_stringhe]

def main():
    ip_Utente = input("Indirizzo IP: ")
    subnet_mask = input("Subnet Mask: ")
    in_sub = input("inserire numero di sottoreti: ")
    indirizzoIP = IPadress(ip_Utente)
    #print(f"{indirizzoIP.ip_dec},{indirizzoIP.ip_bin}")
    #print(f"{indirizzoIP.toList()}")
    print(f"IP decimale: {indirizzoIP.ip_dec}")
    print(f"IP binario: {indirizzoIP.dec2bin()}\n")
    print(f"IP broadcast decimale: {bin2dec(indirizzoIP.ip_broadcast(subnet_mask))}")
    print(f"IP rete decimale: {bin2dec(indirizzoIP.ip_rete(subnet_mask))}")

if __name__ == "__main__":
    main()