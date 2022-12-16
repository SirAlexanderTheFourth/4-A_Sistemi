def covid():
    file=open("covid-19_gen1.txt","r")
    lista_righe=file.readlines()
    file.close()
    string_covid=""
    for riga in lista_righe:
        string_covid=string_covid+riga
    A, C, G, T=0
    for letter in string_covid:
        if(letter=='A'):
            A=A+1
        elif(letter=='C'):
            C=C+1
        elif(letter=='G'):
            G=G+1
        elif(letter=='T'):
            T=T+1
