"""esempio di dictionary comprehension"""
from random import randint
students = ("anna", "marco", "luciano", "giuseppe", "pasquale")

score = {item:randint(40, 100) for item in students }
print (score)
passed_student = {key:value for (key, value) in score.items() if value > 50 }
print (passed_student)


