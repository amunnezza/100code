try:
    file = open("./day30/NonEsiste1.txt") 
    a_dict = {{"key": "valu"}}
    print (a_dict["nonEsiste"])
        
except: #intercetta errore nel dizionario ma non è quello che voglio
    with open("./day30/NonEsiste1.txt", "a") as file3:
        file3.write("prova di esecuzione\n")