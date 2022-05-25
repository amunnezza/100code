try:
    file = open("./day30/NonEsiste1.txt") 
    a_dict = {"key": "valu3"}
    print (a_dict["nonEsiste"])
        
except FileNotFoundError:
    file = open("./day30/NonEsiste1.txt", "a") 
    file.write("prova di esecuzione\n")
# except KeyError:
#     a_dict["nonEsiste"] = "oraEsiste"
#     print (a_dict["nonEsiste"])
except KeyError as error_message: 
    print (f"the key {error_message} does not exist. Lo creo io")
    a_dict[error_message] = "valoreNuovo"
else:
    content = file.read()
    print (content)
finally: 
    file.close()
    print ("file have been closed")