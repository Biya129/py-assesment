class Reply:
    def __init__(self, user, text):
        self.user = user
        self.text = text

class Comment:
    def __init__(self, user, text):
        self.user = user
        self.text = text
        self.reply = None

    def add_reply(self, reply):
        if self.reply is None:
            self.reply = reply
        else:
            print("Cannot add another reply.")
