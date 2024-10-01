from video import Video

class ShortVideo(Video):
    MAX_LENGTH = 60

    def __init__(self, title, description, length, channel):
        super().__init__(title, description, length, channel)
        self.comments = []
        if length > ShortVideo.MAX_LENGTH:
            raise ValueError(f"Short video cannot exceed {ShortVideo.MAX_LENGTH} seconds.")
        self.dimensions = "portrait"
