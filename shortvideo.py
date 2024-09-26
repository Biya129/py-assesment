from video import Video

class ShortVideo(Video):
    def __init__(self, title, description, length, channel):
        super().__init__(title, description, length, channel)
        self.comments = []
        if length > 60:
            raise ValueError("Short video cannot exceed 60 seconds.")
        self.dimensions = "portrait"