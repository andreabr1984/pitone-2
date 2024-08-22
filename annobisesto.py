anno = int(input("Inserisci l'anno. "))
if (anno %4 == 0 and anno %100 != 0) or (anno %400 == 0 ): 
    print("anno è bisiesitle")else:
    print("no bisesitle")
    

