class Telebot:

    def __init__(self):
        pass

    @staticmethod
    def cmd_input(inp):
        if inp == "Привет":
            return "Hay!"
        elif inp == "Пока":
            return "Bye!"
        else:
            return "I don't understand! Sorry!"
