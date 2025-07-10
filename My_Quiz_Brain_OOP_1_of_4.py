# Big Thanks You!!! to Dr. Angela Yu, Developer and Lead Instructor. My instructor at Udemy. Because of her help I can code.
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain,

question_bank = []
for key in question_data:
    key_tx = key["text"]
    key_ans = key["answer"]
    new_question = Question(key_tx, key_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
else:
    print("You have completed the Quiz!")
    print(f"Your final score is{quiz.score}/{quiz .q_number}")
