#from quiz_brain import QuizBraint

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for dato in question_data :
    new_question = Question (dato["text"], dato["answer"])
    question_bank.append(new_question)
# per testprint (question_bank)
#fine 157 torna a cherrytree

#PUNTO 1 venendo da quiz_brain.py

quiz = QuizBrain(question_bank)
#TORNA A QUIZBRAIN.PY
#PUNTO 2 
quiz.next_question()      
# e fino a qui interfaccia funziona come volevo
# fine video 158
#mettiamo ora una cosa del TIPo 
# while (if quiz has still question da fare in quizbrain)
# quiz.next_question()
while quiz.still_has_questions():
    quiz.next_question()


print ("you have completed the quiz")
print (f"Your final score is {quiz.score}/{quiz.question_number}")

#160 ora vai a cherrytree