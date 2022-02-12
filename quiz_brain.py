class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def questions_remaining(self):
        if self.question_number < len(self.questions_list):
            return True
        else:
            return False

    def check_answer(self, guess, answer):
        if guess.lower() == answer.lower():
            print(f"Correct, the answer is {guess}")
            self.score += 1
        else:
            print(f"Incorrect, the answer is {answer}")
        print(f"Your current score is {self.score}/{self.question_number} for {len(self.questions_list)} questions")
        print("\n")




    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        guess = input(f"Q.{self.question_number} {current_question.text} -> ")
        self.check_answer(guess, current_question.answer)









