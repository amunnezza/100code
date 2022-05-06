# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
import pandas as pd
#{"A": "Alfa", "B": "Bravo"}
data_frame = pd.read_csv("./day26/natoAlfabeth/nato.csv")
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#print (data_frame)
data_dict = data_frame.to_dict()
#print (data_dict)

phonetic_dict = {row.letter:row.code for (index, row) in data_frame.iterrows()}

#print (phonetic_dict)
word = input ("insert a word ").upper()

output_list = [phonetic_dict[letter]  for letter in word]
print (output_list)