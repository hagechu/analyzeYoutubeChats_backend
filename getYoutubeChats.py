import pytchat
import time


def getYoutubeChats(videoID):
    chat = pytchat.create(video_id=videoID)
    start_time = time.perf_counter()

    while chat.is_alive():
        for c in chat.get().items:
            print(f"{c.datetime} [{c.author.name}]- {c.message}")

    end_time = time.perf_counter()
    print("end")
    elapsed_time = end_time - start_time
    print(elapsed_time)

# dj2xt5wSA7A
# HFi7I-Z-86E


getYoutubeChats('dj2xt5wSA7A')
