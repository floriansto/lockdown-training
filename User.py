class User:
    def __init__(self, chat_id=-1, user=None, from_dict=None):
        if from_dict is None:
            self.chat_id = chat_id
            self.user_name = user.username
            self.full_name = user.full_name
        else:
            self.chat_id = from_dict["chat_id"]
            self.user_name = from_dict["user_name"]
            self.full_name = from_dict["full_name"]

    def __eq__(self, other):
        return (self.chat_id == other.chat_id and
                self.user_name == other.user_name and
                self.full_name == other.full_name)

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

    def set_user_name(self, user_name):
        self.user_name = user_name

    def set_full_name(self, full_name):
        self.full_name = full_name

    def get_chat_id(self):
        return self.chat_id

    def get_user_name(self):
        return self.user_name

    def get_full_name(self):
        return self.full_name

    def get_dict(self) -> dict:
        return {"chat_id": self.chat_id,
                "user_name": self.user_name,
                "full_name": self.full_name}