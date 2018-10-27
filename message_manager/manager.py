
class Message:

    def __init__(self, msg_json):
        self.update_id = self.get_update_id(msg_json)
        self.chat_id = self.get_chat_id(msg_json)
        self.text = self.get_text(msg_json)
        self.user_name = self.get_user_name(msg_json)

    @staticmethod
    def get_update_id(message_json):
        return message_json['update_id']

    @staticmethod
    def get_user_name(message_json):
        return message_json['message']['chat']['first_name']

    @staticmethod
    def get_text(message_json):
        return message_json['message']['text']

    @staticmethod
    def get_chat_id(message_json):
        return message_json['message']['chat']['id']