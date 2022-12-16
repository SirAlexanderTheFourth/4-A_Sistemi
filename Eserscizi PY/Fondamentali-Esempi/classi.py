class IPadress():
    def __init__(self, ip_stringa):
        self.ip_notazione_dec = ip_stringa
        self.ip_notazione_bin=None  
        self.ip_binario=None

    def toList(self):
        lista_stringhe=self.ip_notazione_dec.split(".")
        return [int(gruppo) for gruppo in lista_stringhe]

    def dec2bin(self):
        lista_stringhe=self.ip_notazione_dec.split(".")
        lista_gruppi=[int (gruppo) for gruppo in lista_stringhe]
        s=""
        for gruppo in lista_gruppi:
            temp=bin(gruppo)[2:]
            temp="0"*(8-len(temp))+temp
            s=s+temp+"."
        self.ip_binario=s[:-1]
        return s[:-1]
    
    def bin2dec(self):
        lista_bin_rete=ip.split(".")
        d=""
        for num in lista_bin_rete
    
    def ip_broadcast(self, subnet_mask="/24"):
        sub=int(subnet_mask[1:])
        host=32-sub
        bi_r=bin(sub)
        bi_h=bin(host)
        mask=""
        mask=
        for i in range(0, 32):
            if(i%8==0 and i!=0):
                mask= mask + "."
            if i < sub :
                mask=mask+"0"
            elif i >= host:
                mask=mask+"1"
        broadcast=""
        for m, i in zip(mask, self.ip_binario):
            if m == 0:
                
        return mask

        


def main():
    indirizzoIP=IPadress("192.168.0.123")
    print(indirizzoIP)
    print(indirizzoIP.toList())
    print(indirizzoIP.dec2bin())
    print(indirizzoIP.ip_broadcast())

if __name__=="__main__":
    main()
