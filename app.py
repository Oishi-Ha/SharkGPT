import os
from flask import Flask, render_template, request, jsonify
from langchain.llms import OpenAI
from dotenv import load_dotenv
from pathlib import Path

app = Flask(__name__)
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

openai_api_key = os.getenv("OPENAI_API_KEY")


def generation_to_dict(generation):
    # Assuming that 'generation' has the properties 'id', 'text', and 'tokens'
    return {
        "id": generation.id,
        "text": generation.text,
        "tokens": generation.tokens,
    }


def runinfo_to_dict(runinfo):
    # Assuming that 'runinfo' has the property 'run_id'
    return {
        "run_id": runinfo.run_id,
    }


def llmresult_to_dict(llmresult):
    return {
        "generations": [[generation_to_dict(g) for g in gen_list] for gen_list in llmresult.generations],
        "llm_output": llmresult.llm_output,
        "run": runinfo_to_dict(llmresult.run) if llmresult.run else None,
    }


@app.route('/', methods=("GET", "POST"))
def index():
    return render_template("index.html")


@app.route('/chat', methods=['POST'])
def chat():
    prompt = request.form['message']
    llm = OpenAI(model_name="text-davinci-003", temperature=0.9)
    response = llm.generate([prompt], api_key=openai_api_key)

    return jsonify(llmresult_to_dict(response))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
