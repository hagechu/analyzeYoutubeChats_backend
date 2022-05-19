from flask import Flask
from flask import request, make_response, jsonify
from flask_cors import CORS
from getYoutubeChats import getYoutubeChats

app = Flask(__name__)
CORS(app)
