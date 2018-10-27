from questions.get_question import GetQuestion


class Telebot:

    def __init__(self):
        self.question = GetQuestion()

    def cmd_input(self,inp):

        if inp == "Привет":
            return "Hay!"
        elif inp == "Пока":
            return "Bye!"
        elif inp == "question":
            return self.question.get_question()
        else:
            return "I don't understand! Sorry!"
