import pytchat


def getYoutubeChats(videoID):
    chats = []
    chatsDict = {}
    chat = pytchat.create(video_id=videoID)

    while chat.is_alive():
        for c in chat.get().items:
            chats.append(
                {"date": c.datetime, "name": c.author.name, "message": c.message})

    chatsDict = {"chats": chats}

    return chatsDict

# "dj2xt5wSA7A"
# "HFi7I-Z-86E"
