from flask import Flask
from flask import request, make_response, jsonify
from flask_cors import CORS
from markupsafe import Markup
from getYoutubeChats import getYoutubeChats
from getYoutubeChatsTest import getYoutubeChatsTest

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])


@app.route("/", methods=['GET'])
def index():
    html = '''
    <p> 動いてます </p>
    '''
    return Markup(html)


@app.route("/getYoutubeChats", methods=['GET', 'POST'])
def responseYoutubeChats():
    data = request.get_json()
    videoID = data['videoID']

    response = getYoutubeChats(videoID)

    return make_response(jsonify(response))


@app.route("/getYoutubeChatsTest", methods=['GET', 'POST'])
def responseYoutubeChatsTest():
    data = request.get_json()
    videoID = data['videoID']

    response = getYoutubeChatsTest(videoID)

    return make_response(jsonify(response))


if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=5000, use_reloader=False, threaded=False)

# http://127.0.0.1:5000
# http://127.0.0.1:5000/getYoutubeChats
