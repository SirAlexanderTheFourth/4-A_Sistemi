alfabeto={"a":"b","b":"c","c":"d","d":"e","e":"f","f":"g","g":"h","h":"i","i":"l","l":"m","m":"n","n":"o","o":"p","p":"q","q":"r","r":"s","s":"t","t":"u","u":"v","v":"z","z":"a"}
messaggio=input("inserire messaggio: ")
messaggio_tradotto=""

for lettera in messaggio:
    messaggio_tradotto=(messaggio_tradotto+alfabeto[lettera])

print(f"il messaggio tradotto è: {messaggio_tradotto}")
decodificatore=dict({})
#dizionario.items()
for k,v in alfabeto.items():
    decodificatore[v]=k

print(decodificatore)
messaggio_decriptato=""

for lettera in messaggio_tradotto:
    messaggio_decriptato=(messaggio_decriptato+decodificatore[lettera])

print(f"il messaggio decriptato è: {messaggio_decriptato}")