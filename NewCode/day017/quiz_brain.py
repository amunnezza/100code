# TODO : asking the questions

# TODO check if answer is right

# TODO check if we are to end of the quiz

class QuizBrain:
    def __init__(self, question_list):
        self.question_number =  0
        self.question_list = question_list
        self.score = 0
#pronta da usare in main.py e vai li al punto  1       
    def next_question (self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input (f"Q.{self.question_number } : {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)  
# si tratta ora di chiamare le funzioni adatte in main.py
#vai a main.py in punto 2

#create a method still_has_question return boolean 
# to use in while loop of main.py
    def still_has_questions(self):
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False
        return self.question_number < len(self.question_list)

#rimane da mettere attributo score e methodo for 
#check of answer
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print ("You got it right")
            self.score += 1
        else:
            print ("YOu got it wrong")
        print (f"the correct answer was {correct_answer}") #fatto
        print (f"Your current score is: {self.score}/{self.question_number} ")
    #rimane da definire score
