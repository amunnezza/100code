#gia visto come iterare su un dictionary

student_dict = {"student":["angela", "mary", "alex"], 
                "vote":[58, 66, 77]}

#loop trhough dictionaries

for (key, value) in student_dict.items():
    print (key)
    print (value)

''' In qualche modo anche dataframe somiglia a iterare su dictionary'''

import pandas as pd
#crea dataframe dal dizionario gia visto in precedenza
student_data_frame = pd.DataFrame (student_dict)
print (student_data_frame)

#ora per iterare sul dataframe

for (key,value) in student_data_frame.items():
    print (key)     #stampa nomi colonne    

    print (value)    #stampa valori in colonne
    
    #tutto cio non molto utile e quindi panda ha un built in loop
    #un metodo iterrows che ritorna il numero di riga e il contenuto
    #della riga

for (index, row) in student_data_frame.iterrows():
    #print (index)
    print (row)# ognuna di questa row è un panda vector e quindi posso tap 
                #su un particolare colonna del vettore 
                #per esempio se sono interessanto a nome studente
                #posso scrivere
    print (row.student) #vale anche per score e posso anche fare 
                        #una cosa del tipo

    if row.student == "angela":
        print (f"il voto di angela è {row.vote}")
