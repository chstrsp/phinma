from Question import Question
import random

question_list = [
    Question("whats my name", "irvin"),
    Question("whats my age", "11"),
    Question("whats my gender", "male")
]

def get_random_question():
    sentence = random.choice(question_list)
    return sentence


'''for i in question_list:
    print(i.get_question())
    print(i.get_answer())'''
