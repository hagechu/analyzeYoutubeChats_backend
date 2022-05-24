from crypt import methods
from urllib import response
from flask import Flask
from flask import request, make_response, jsonify
from flask_cors import CORS
from markupsafe import Markup
from getYoutubeChats import getYoutubeChats

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
    response = getYoutubeChats("HFi7I-Z-86E")

    return make_response(jsonify(response))


if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=5000, use_reloader=False, threaded=False)

# http://127.0.0.1:5000
# http://127.0.0.1:5000/getYoutubeChats
