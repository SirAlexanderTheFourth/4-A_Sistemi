def leggi_file(nome_file):
    file=open(nome_file,"r")
    lista_righe=file.readlines()
    file.close()

    diz_matematici={"id":[], "nomi":[]} #id numeri, nomi str

    for riga in lista_righe[1:]:
        #linea senza \n
        riga_senza_n=riga[:-1]
        lista_campi=riga_senza_n.split(",") 
        print(lista_campi)
        id=int(lista_campi[0])
        nome=lista_campi[1]
        diz_matematici["id"].append(id)
        diz_matematici["nomi"].append(nome[1:])
    return diz_matematici

def nomeID(id, diz):
    listaID=diz["id"]
    listanomi=diz["nomi"]
    for i, n in zip(listaID, listanomi):
        if i==id:
            return n


    """
    for k,v in diz.items():
        if(k==id):
            return v
    """

def main():
    diz=leggi_file("./matematici.csv")
    print(diz)
    id=2
    nome=nomeID(id, diz)
    print(nome)

if __name__=="__main__":
    main()
