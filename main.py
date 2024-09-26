from channel import Channel
from user import User
from video import Video
from shortvideo import ShortVideo
from comment import Comment


if __name__ == "__main__":
    
    user1 = User("Bisma")
    user2 = User("Wahab")

    channel1 = user1.create_channel("Bisma's Channel")

    video1 = channel1.upload_video("My First Video", "This is my first video!", 120)
    short1 = channel1.upload_video("My First Short", "A quick short video", 45, is_short=True)

    user2.subscribe_to_channel(channel1)

    video1.like_video()
    comment1 = user2.post_comment(video1, "What an Informative Video!")

    reply1 = user1.reply_to_comment(comment1, "Thank you so much!")

    video1.show_comments()

    channel1.display_subscribers()

