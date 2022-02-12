from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import giraffe, quiz_time_art
import random

# This is a way to randomize questions with repeat, which obviously was a bad idea, because of repeat...
# random_qa = random.choice(question_data)
# question_random_text = random_qa["text"]
# answer_random_text = random_qa["answer"]

question_bank = [Question(question['text'], question['answer']) for question in question_data]
# print((question_bank[0]).text) - This shows if an indexed question_bank object is working

quiz_time = QuizBrain(question_bank)

print(quiz_time_art)

while quiz_time.questions_remaining():
    quiz_time.next_question()
    print(giraffe)


print("Congratulations, you have completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number} for {len(quiz.questions_list)}questions")

# new_q = Question(question_random_text,answer_random_text)
#
# print(question_random_text, answer_random_text)
