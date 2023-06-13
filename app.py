import os
import openai
from flask import Flask, render_template, request
from langchain.llms import OpenAI

app = Flask(__name__)
openai_api_key = os.getenv("OPENAI_API_KEY")


@app.route('/', methods=("GET", "POST"))
def index():
    return render_template("index.html")


@app.route('/chat', methods=['POST'])
def chat():
    prompt = request.form['message']

    # Llms
    llm = OpenAI(openai_api_key='your_api_key', temperature=0.9)

    # Show stuff to the screen if there's prompts
    if prompt:
        response = llm(prompt)
    return response


if __name__ == '__main__':
    app.run()
