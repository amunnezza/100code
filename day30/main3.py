try:
    file = open("./day30/NonEsiste1.txt") 
    a_dict = {"key": "valu3"}
    print (a_dict["nonEsiste"])
        
except FileNotFoundError:
    with open("./day30/NonEsiste1.txt", "a") as file3:
        file3.write("prova di esecuzione\n")
except KeyError:
    a_dict["nonEsiste"] = "oraEsiste"
    print (a_dict["nonEsiste"])