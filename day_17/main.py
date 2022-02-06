import data as data
from question_model import Question
from quiz_brain import QuizBrain

data_list = data.question_data
quiz_brain = QuizBrain(data_list)


def get_all_questions(question_lst):
    """Creates a list of question objects from the data.py file"""
    question_bank = []
    for item in question_lst:
        question = Question(item["question"], item["correct_answer"])
        question_bank.append(question)
    return question_bank


def run():

    correct_questions = 0

    while quiz_brain.still_got_questions():
        current_question = quiz_brain.next_question()
        user_answer = input(f"Q.{quiz_brain.question_number}: {current_question['question']} (True/False): ")
        if user_answer == current_question["correct_answer"]:
            print("You got it right!")
            correct_questions += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {current_question['correct_answer']}")
        print(f"Your current score is {correct_questions}/{quiz_brain.question_number}")
    print(f"Your score: {correct_questions}/{quiz_brain.question_number}")


run()
