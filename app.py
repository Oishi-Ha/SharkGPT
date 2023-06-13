import os
from flask import Flask, render_template, request, jsonify
from langchain.llms import OpenAI
from dotenv import load_dotenv
from pathlib import Path

app = Flask(__name__)
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

openai_api_key = os.getenv("OPENAI_API_KEY")


@app.route('/', methods=("GET", "POST"))
def index():
    return render_template("index.html")


@app.route('/chat', methods=['POST'])
def chat():
    prompt = request.form['message']
    llm = OpenAI(model_name="text-davinci-003", temperature=0.9)
    response = llm.generate([prompt], api_key=openai_api_key)

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
