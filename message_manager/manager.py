
class Message:

    @staticmethod
    def get_update_id(message_json):
        return message_json['update_id']

    @staticmethod
    def get_name(message_json):
        return message_json['message']['chat']['first_name']

    @staticmethod
    def get_text(message_json):
        return message_json['message']['text']

    @staticmethod
    def get_chat_id(message_json):
        return message_json['message']['chat']['id']