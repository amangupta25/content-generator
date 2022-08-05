import os
import openai
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

openai.api_key = os.environ['OPEN_AI_KEY']

@app.route("/")
def index():
    return "Hello World!"

@app.route('/getContent/', methods=['POST'])
def get_content():
    try:
        record = json.loads(request.data)
        response = openai.Completion.create(
                model="text-davinci-002",
                prompt=record['prompt'],
                temperature=0.5,
                max_tokens=60,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
              )
    except:
        print("An exception occurred")
    return jsonify({"status" : "ok", "result" : strip(response.choices[0].text) })
