class Video:
    def __init__(self, title, description, length, channel):
        self.title = title
        self.description = description
        self.length = length
        self.channel = channel
        self.likes = 0
        self.comments = []
    
    def like_video(self):
        self.likes += 1
    
    def show_comments(self):
        for comment in self.comments:
            print(f"{comment.user.username}: {comment.text}")
            if comment.reply:
                print(f"  Reply -> {comment.reply.user.username}: {comment.reply.text}")