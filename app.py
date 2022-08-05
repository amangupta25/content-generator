import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

openai.api_key = "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"

@app.route("/")
def index():
    return "Hello World!"

@app.route('/getContent/<string:prompt>/', methods=['GET'])
def get_content(prompt):
#     response = openai.Completion.create(
#         model="text-davinci-002",
#         prompt=prompt,
#         temperature=0.5,
#         max_tokens=60,
#         top_p=1.0,
#         frequency_penalty=0.0,
#         presence_penalty=0.0
#       )
#     return jsonify({"status" : "ok", "result" : response.choices[0].text })
    return prompt
