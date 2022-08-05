import json
from flask import Flask, request, jsonify

app = Flask(__name__)

openai.api_key = "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"

@app.route("/")
def index():
    return "Hello World!"

@app.route('getContent/<string:prompt>/', methods=['GET'])
def get_content(prompt):
    record = json.loads(request.data)
