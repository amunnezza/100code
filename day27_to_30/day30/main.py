# with open("./day30/prova.txt") as file:
#     result = file.read()
#     print (result)
#FileNotFoundError
# with open ("./day30/nonEsiste.txt") as file2:
#     file2.read()
try:
    with open("./day30/NonEsiste1.txt") as file3:
        result2 = file3.read()
        print(result2)
except: #se non c e apri in scrittura che lo crea in auto
    with open("./day30/NonEsiste1.txt", "w") as file3:
        file3.write("prova di esecuzione")
        


# KeyError
# a_dict = {"key":"value"}
# value = a_dict["nonExistentKey"]

# IndexError
# fruit_list = ["banana", "mela", "arancia"]
# print (fruit_list[3])
