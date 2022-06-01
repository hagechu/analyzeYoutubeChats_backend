import testData1
import testData2
import testData3


def getYoutubeChatsTest(videoID):
    if videoID == "HFi7I-Z-86E":
        chatsDict = {"chats": testData1.testData1}
    elif videoID == "dj2xt5wSA7A":
        chatsDict = {"chats": testData2.testData2}
    else:
        chatsDict = {"chats": testData3.testData3}

    return chatsDict
