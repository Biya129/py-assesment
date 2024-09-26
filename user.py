from channel import Channel
from comment import Comment

class User:
    def __init__(self, username):
        self.username = username
        self.channels = []
        self.subscribed_channels = []
    
    def create_channel(self, name):
        channel = Channel(name, self)
        self.channels.append(channel)
        return channel
    
    def subscribe_to_channel(self, channel):
        if channel not in self.subscribed_channels:
            self.subscribed_channels.append(channel)
            channel.subscribers.append(self)
            print(f"{self.username} subscribed to {channel.name}")
    
    def post_comment(self, video, text):
        comment = Comment(self, text)
        video.comments.append(comment)
        return comment
    
    def reply_to_comment(self, comment, text):
        if comment.reply is None: 
            reply = Comment(self, text)
            comment.reply = reply
            return reply
        else:
            print("Cannot reply to a reply.")
            return None