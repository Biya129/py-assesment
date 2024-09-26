from shortvideo import Video, ShortVideo

class Channel:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.videos = []
        self.subscribers = []

    def upload_video(self, title, description, length, is_short=False):
        if is_short:
            video = ShortVideo(title, description, length, self)
        else:
            video = Video(title, description, length, self)
        self.videos.append(video)
        return video

    def display_subscribers(self):
        print(f"Subscribers to {self.name}: {[user.username for user in self.subscribers]}")