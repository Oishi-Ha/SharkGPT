import os
# import openai
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
    llm = OpenAI(api_key=openai_api_key, temperature=0.9)

    # Show stuff to the screen if there's prompts
    if prompt:
        response = llm(prompt)
        return response

    return ""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
