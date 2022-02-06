class QuizBrain:

    def __init__(self, q_lst):
        self.q_lst = q_lst
        self.question_number = 0

    def next_question(self):
        """Retrieve the item at the current question number from question list."""
        current_number = self.question_number
        item = self.q_lst[current_number]
        self.question_number += 1
        return item

    def still_got_questions(self):
        """Check whether the question list is fully explored"""
        if self.question_number == len(self.q_lst):
            return False
        else:
            return True
