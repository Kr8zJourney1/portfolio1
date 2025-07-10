class QuizBrain:
    def __init__(self,question_list):
        self.q_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.q_number < len(self.question_list)
        # if self.q_number < len(self.question_list):
        #     return True
        # else:
        #     False

    def next_question(self):
        current_q = self.question_list[self.q_number]
        user_answer = input(f"Q.{self.q_number + 1 }:{current_q.text} (True or False):")
        self.check_answer(user_answer, current_q.answer)
        # print(currentq)

    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You are correct!")
        else:
            print("That's wrong")
        print(f"the correct answer is{correct_answer}")
        print(f"Your score is {self.score}/{self.q_number}")
        print("\n")
