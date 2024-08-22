import socket as soc

target= input("Dammi l'IP macchina da scansire. ")
portrange = input("Inserisci un port range(es 5-200)")
lowport = 5
highport = 200
if "-" in portrange:
    lowport =int(portrange.split('-')[0])
    highport= int(portrange.split('-')[1])

print("Scansisco host:",target,"dalla porta",lowport,"alla porta", highport)

for port in range(lowport,highport+1):
    s=soc.socket(soc.AF_INTET,soc.SOCK_STREAM)
    status= s.connect_ex((target, port))
    if(status==0):
        print("***Porta", port,"-Aperta***")
    else:
        print("port",port,"CHIUSA")
    s.close()

    

