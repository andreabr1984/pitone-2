def offerte()
    lista_offerte ["Giga illimitati", "chiamate all'estero","500SMS"]
    a=0
    for offerta in lista_offerte:
        a +=1
        print (a,offerta)

def servizio_tecnico(Numeroditelefono):
    if Numeroditelefono.stratrswith(0): 
        print("Benvenuto")
    
    
    
    